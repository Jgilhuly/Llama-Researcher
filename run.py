import asyncio

from dotenv import load_dotenv

from llama_index.utils.workflow import draw_all_possible_flows
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

from workflow import ResearchAssistantWorkflow


async def main():
    load_dotenv()
    llm = OpenAI(model="gpt-4o-mini")
    embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    workflow = ResearchAssistantWorkflow(
        llm=llm, embed_model=embed_model, verbose=True, timeout=60.0
    )
    # draw_all_possible_flows(workflow, filename="research_assistant_workflow.html")
    res = await workflow.run(query="Widevine DRM")
    print(res)


if __name__ == "__main__":
    asyncio.run(main())
