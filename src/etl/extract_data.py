import requests
import os
import json
from pathlib import Path
from datetime import datetime
from config.settings import FILES_FOLDER_RAW
from src.utils.logger import logger

def extract_anp_data(output_path: Path, execution_dt: str = None):
    """
    Extrai dados da API de revendedores de combustíveis da ANP e salva em arquivo JSON.

    :param output_path: Caminho completo onde o JSON será salvo.
    :param execution_dt: Timestamp da execução (para logs ou metadados).
    """

    url = "https://revendedoresapi.anp.gov.br/v1/combustivel"
    
    headers = {
        "User-Agent": "etl-anp-pipeline/1.0",
        "Accept": "application/json",
        "Connection": "keep-alive"
    }

    try:
        logger.info(f"📡 Requisitando dados da API ANP: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        logger.error(f"❌ Erro ao acessar a API de revendedores da ANP: {e}")
        raise

    os.makedirs(FILES_FOLDER_RAW, exist_ok=True)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"✅ Dados ANP (revendedores) salvos com sucesso em: {output_path}")
    except Exception as e:
        logger.error(f"❌ Erro ao salvar JSON da ANP: {e}")
        raise
