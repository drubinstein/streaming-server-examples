from typing import Iterator
from concurrent import futures
import grpc

from vector_stream_pb2 import RequestResponse
import vector_stream_pb2_grpc


class VectorStreamServicer(vector_stream_pb2_grpc.VectorStreamServicer):
    def add_one(
        self, request_iterator: Iterator[RequestResponse], context
    ) -> Iterator[RequestResponse]:
        for request in request_iterator:
            yield RequestResponse(data=[1 + d for d in request.data])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vector_stream_pb2_grpc.add_VectorStreamServicer_to_server(
        VectorStreamServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
