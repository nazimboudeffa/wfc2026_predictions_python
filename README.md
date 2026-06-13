# WFC 2026 Predictions

Projet de base pour preparer des donnees de football et tester un modele de prediction dans un notebook Jupyter.

## Fichiers du projet

- MatchPredictionNotebook_v2.ipynb : notebook principal a executer
- PLAN_DE_TRAVAIL.md : plan de travail

## Execution en local (environnement Python)

### 1. Prerequis

- Python 3.10+ installe
- VS Code avec les extensions Python et Jupyter

### 2. Creer et activer un environnement virtuel

Sous Windows PowerShell, dans le dossier du projet :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Installer les dependances

```powershell
pip install --upgrade pip
pip install jupyter pandas numpy requests python-dotenv scikit-learn
```

### 4. Configurer la cle API (optionnel pour la partie placeholder)

Creer un fichier .env a la racine du projet avec :

```env
API_FOOTBALL_KEY=ta_cle_api_ici
```

### 5. Ouvrir et executer le notebook

1. Ouvrir MatchPredictionNotebook_v2.ipynb dans VS Code.
2. Cliquer sur Select Kernel (en haut a droite).
3. Choisir le kernel Python de .venv.
4. Executer les cellules une par une (bouton Run) ou Run All.

## Execution depuis GitHub

### Option A - Visualisation simple sur GitHub.com

GitHub affiche le notebook, mais ne l execute pas.

### Option B - Execution avec GitHub Codespaces

1. Ouvrir le depot sur GitHub.
2. Cliquer sur Code, puis Codespaces, puis Create codespace.
3. Dans le terminal du Codespace :

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install jupyter pandas numpy requests python-dotenv scikit-learn
```

4. Ouvrir MatchPredictionNotebook_v2.ipynb et choisir le kernel .venv.
5. Executer les cellules.

### Option C - Ouvrir le notebook dans Google Colab

1. Sur GitHub, ouvrir MatchPredictionNotebook_v2.ipynb.
2. Copier l URL du fichier notebook.
3. Dans Colab : File > Open notebook > GitHub ou URL.
4. Installer les dependances dans une cellule si necessaire :

```python
!pip install pandas numpy requests python-dotenv scikit-learn
```

## Depannage rapide

- Erreur Unexpected token # : le fichier n est pas un vrai JSON notebook. Utiliser MatchPredictionNotebook_v2.ipynb.
- Kernel introuvable : reinstaller les extensions Python/Jupyter puis recharger VS Code.
- Module not found : verifier que les paquets sont installes dans le meme environnement que le kernel.