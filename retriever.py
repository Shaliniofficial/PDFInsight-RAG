import faiss
import numpy as np

def create_index(vectors):

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(vectors)

    return index


def retrieve_chunks(
    index,
    query_vector,
    chunks,
    k=3
):

    distances, indices = index.search(
        np.array([query_vector]),
        k
    )

    results = []

    for idx in indices[0]:

        results.append(
            chunks[idx]
        )

    return results