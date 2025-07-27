from datetime import datetime
from pathlib import Path
from src.etl.extract_data import extract_anp_data
from config.settings import FILES_FOLDER_RAW
from src.utils.logger import logger

def main():
    logger.info("🚀 Iniciando processo de extração de dados da ANP...")

    # Cria o nome do arquivo com timestamp
    execution_dt = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = Path(FILES_FOLDER_RAW) / f"revendedores_combustivel_{execution_dt}.json"

    # Executa a extração
    extract_anp_data(output_file, execution_dt)

    logger.info("🏁 Extração concluída com sucesso.")

if __name__ == "__main__":
    main()
