from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
vars = {**dotenv_values(".env"),
        **dotenv_values(".env.secret")}
print(vars['HOST'])