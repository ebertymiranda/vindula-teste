from celery import shared_task
import pandas as pd
from .models import Filme

@shared_task
def importar_planilha_excel(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        title = row['Title']
        Filme.objects.get_or_create(title=title)

    print("Importação concluída")
