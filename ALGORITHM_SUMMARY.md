## ⚽ Algorithme de Prédiction des Scores de Football (World Cup)

Ce document décrit la méthodologie complète implémentée pour prédire les scores potentiels des matchs, en utilisant une approche statistique multi-couches. L'algorithme est structuré en trois phases majeures : Force Équipe ($\text{ELO}$), Buts Attendus ($\lambda$), et Prédiction Finale (Poisson).

### 🎯 Objectif
Estimer de manière robuste le score final probable entre deux équipes, en allant au-delà d'une simple corrélation des buts passés.

### 🛠 Structure Algorithmique (Point 3)

#### Phase 1 : Calcul du Rating ELO (Force Relative)
Le rating Elo est crucial pour établir une mesure de force fiable et comparable entre toutes les équipes, quel que soit le contexte ou la compétition.
*   **Concept :** Il s'agit d'un système de classement qui ajuste la note de chaque équipe après **chaque match**. Les victoires contre des adversaires forts entraînent un gain important de rating.
*   **Fonctionnement dans l'algorithme :** La fonction `calculate_elo` itère sur tous les matchs historiques (sempre le contexte World Cup). Elle calcule la déviation du score réel par rapport au score attendu basé uniquement sur le différentiel des ratings actuels ($\text{ELO}_{\text{A}} - \text{ELO}_{\text{B}}$). Cette déviation est utilisée pour ajuster le rating de chaque équipe.

#### Phase 2 : Estimation des Buts Attendus ($\lambda$ - Expected Goals)
Cette phase convertit la force abstraite (les points Elo) en un taux physique mesurable et interprétable : les buts attendus pour chaque équipe par match.
*   **Formule Clé :** Nous utilisons une relation de proportionnalité basée sur le différentiel de rating :
    $$\lambda_{Home} = \max(0.8, 1 + \frac{\text{HomeRating} - \text{AwayRating}}{900})$$
*   **Signification :** $\lambda_{Home}$ ne représente pas les buts *réels*, mais le nombre moyen de buts que l'équipe à domicile devrait marquer en moyenne. Une différence élevée de rating implique un $\lambda$ élevé pour l'équipe favorite.

#### Phase 3 : Génération du Score Prédit (Distribution de Poisson)
Le score final est une variable aléatoire. Utiliser simplement les $\lambda$ n'est pas suffisant. Nous employons donc la distribution de Poisson, idéale pour modéliser le comptage d'événements discrets (les buts).
*   **Principe :** La probabilité qu'une équipe marque exactement $k$ buts est calculée par :
    $$P(X=k) \, | \, \lambda = \frac{\lambda^k e^{-\lambda}}{k!}$$
*   **Sortie finale :** L'algorithme calcule les valeurs $\lambda_{Home}$ et $\lambda_{Away}$, puis utilise ces valeurs pour **simuler le score final le plus probable** (le point d'espérance) via la fonction `poisson_predict`.

---
### ⚽ Application au Football (Exemple)

Le choix de l'algorithme dépend du phénomène à modéliser :

*   **Classement et Force Relative (Elo) :** Utilisé pour estimer la force intrinsèque des équipes. Chaque match est un "matchup" où le rating Elo prédit les probabilités de victoire, permettant d'ajuster le classement en fonction des surprises ou des confirmations de niveau.
*   **Fréquence d'Événements (Poisson) :** Idéal pour modéliser la fréquence moyenne d'événements rares et indépendants sur une période donnée (ex: nombre moyen de tirs cadrés par match, nombre de corners).
*   **Succès dans un Nombre Fixe d'Essais (Binomial) :** Utilisé lorsque le nombre total de tentatives est connu (ex: analyse des penalties où $n$ est fixe et $p$ est la probabilité de succès).

---
🛠️ **Conclusion Technique :** Le flux de données est séquentiel et dépend tous des éléments précédents. La stabilité du modèle repose sur l'ajustement continu des constantes mathématiques ($K\_FACTOR$, $900.0$) selon un jeu de données plus large (incluant les statistiques xG réelles).