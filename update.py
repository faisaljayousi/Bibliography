"""
This script fetches the references, generates an interactive HTML table, and
saves the output.
"""

import logging

from src import FileSaver, HTMLGenerator, ReferenceFetcher

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    try:
        logging.info("Initialising ReferenceFetcher...")
        fetcher = ReferenceFetcher()
        data, headers = fetcher.fetch_references()
        logging.info("References fetched successfully.")

        logging.info("Initialising HTMLGenerator...")
        generator = HTMLGenerator(data, headers)
        html_content = generator.generate_html_table()
        logging.info("HTML content generated successfully.")

        logging.info("Saving HTML content to file...")
        saver = FileSaver()
        saver.save_html(html_content)
        logging.info("Interactive HTML file generated: references.html")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
