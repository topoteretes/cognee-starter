import os
import asyncio
import pathlib
from cognee import config, add, cognify, search, SearchType, prune, visualize_graph
# from cognee.shared.utils import render_graph

async def main():
    data_directory_path = str(
        pathlib.Path(
            os.path.join(pathlib.Path(__file__).parent, ".data_storage")
        ).resolve()
    )
    # Set up the data directory. Cognee will store files here.
    config.data_root_directory(data_directory_path)

    cognee_directory_path = str(
        pathlib.Path(
            os.path.join(pathlib.Path(__file__).parent, ".cognee_system")
        ).resolve()
    )
    # Set up the Cognee system directory. Cognee will store system files and databases here.
    config.system_root_directory(cognee_directory_path)

    # Prune data and system metadata before running, only if we want "fresh" state.
    await prune.prune_data()
    await prune.prune_system(metadata=True)

    text = "The Python programming language is widely used in data analysis, web development, and machine learning."

    # Add the text data to Cognee.
    await add(text)

    # Cognify the text data.
    await cognify()

    # # Get a graphistry url (Register for a free account at https://www.graphistry.com)
    # url = await render_graph()
    # print(f"Graphistry URL: {url}")

    # Or use our simple graph preview
    graph_file_path = str(
        pathlib.Path(
            os.path.join(pathlib.Path(__file__).parent, ".artifacts/graph_visualization.html")
        ).resolve()
    )
    await visualize_graph(graph_file_path)

    # Completion query that uses graph data to form context.
    graph_completion = await search(query_text="What is python?", query_type=SearchType.GRAPH_COMPLETION)
    print("Graph completion result is:")
    print(graph_completion)

    # Completion query that uses document chunks to form context.
    completion = await search(query_text="What is Python?", query_type=SearchType.COMPLETION)
    print("Completion result is:")
    print(completion)

    # Query all summaries related to query.
    summaries = await search(query_text="Python", query_type=SearchType.SUMMARIES)
    print("Summary results are:")
    for summary in summaries:
        print(summary)

    chunks = await search(query_text="Python", query_type=SearchType.CHUNKS)
    print("Chunk results are:")
    for chunk in chunks:
        print(chunk)


if __name__ == "__main__":
    asyncio.run(main())
