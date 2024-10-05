import openai
import polib
from openai import OpenAI, DefaultHttpxClient
import httpx


def connect_to_gpt(apikey) -> OpenAI:

    # Connection to openAi
    try:
        client = OpenAI(
            api_key=apikey,
            http_client=DefaultHttpxClient(
                proxies="http://192.168.88.111:10809",
                transport=httpx.HTTPTransport(local_address="192.168.88.111"),
                timeout=20.0,
            ),
        )
    except Exception as e:
        print(f"Error creating OpenAI client: {e}")
        return None

    # read fine-tuned file
    # try:
    #     with open("find_tuneds/account_bank_statement_import_csv_translations.jsonl", "rb") as file:
    #         result_ft = client.files.create(
    #             file=file,
    #             purpose="fine-tune"
    #         )
    #     file_id = result_ft.id
    # except FileNotFoundError:
    #     print("Error:fine-tuned File not found.")
    #     return None
    # except Exception as e:
    #     print(f"Error uploading file: {e}")
    #     return None

    # # create fine-tuned
    # try:
    #     fine_tune_job = client.fine_tuning.jobs.create(
    #         training_file=file_id,
    #         model="gpt-4o-2024-08-06"
    #     )
    #     res_id_ftj = fine_tune_job.id[6:]
    # except Exception as e:
    #     print(f"Error creating fine-tune job: {e}")
    #     return None

    # try:
    #     fine_tune_jobs = client.fine_tuning.jobs.list(limit=10)
    # except Exception as e:
    #     print(f"Error listing fine-tune jobs: {e}")
    #     return None

    return client


def chat_gpt_translate(text: str, language: str, client) -> str:
    try:
            
        prompt = f"""
        Translate the following text to {language}, ensuring that all text is translated, including any text within HTML tags.
        Preserve the original HTML tags, special characters such as % and others, and ensure that the number of lines in the translated text matches the number of lines in the original text exactly.

        Original text:
        {text}
        """
        response = client.chat.completions.create(
            # model="ft:gpt-4o-mini:my-org:custom_suffix:id",
            model="gpt-4o-2024-08-06",
            messages=[{"role": "user", "content": prompt}]
        )
        text_translate = (response.choices[0].message.content.strip())
        return text_translate
    except Exception as e:
        print(e)
