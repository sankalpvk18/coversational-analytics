from modelApi import modelApi
from prompt import get_prompt

def get_insight(question):
    db_chain,chain,meta = modelApi()
    prompt=get_prompt(question,meta)
    insight = db_chain.run(prompt)
    return insight