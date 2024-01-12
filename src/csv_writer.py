from scraper import scrape_all_jobs, extract_job_details
from utils import configure_logging
import csv
import logging


def save_to_csv(data, job_urls):
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Job Title', 'Salary', 'Location', 'Views', 'Candidates', 'Job URL', 'Job Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for job_data, job_url in zip(data, job_urls):
            job_data['Job URL'] = job_url
            # Encode non-ASCII characters to prevent UnicodeEncodeError
            encoded_data = {k: v.encode('utf-8').decode('utf-8', 'ignore') if isinstance(v, str) else v
                            for k, v in job_data.items()}
            writer.writerow(encoded_data)


if __name__ == "__main__":
    # Configure logging
    configure_logging('INFO')

    # # Add explicit logging statements
    # logging.info("Logging initialized.")
    # try:
    #     # Introduce an intentional error for testing logging
    #     raise ValueError("This is a deliberate error for testing logging.")
    # except Exception as e:
    #     logging.error(f"Error occurred: {e}")

    # Scraping logic
    url = "https://www.cvbankas.lt/?padalinys%5B%5D=88&keyw="
    data, job_urls = scrape_all_jobs(url)

    # Save data to CSV with job URLs
    save_to_csv(data, job_urls)
