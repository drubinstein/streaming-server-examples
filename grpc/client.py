import grpc
from vector_stream_pb2 import RequestResponse
from vector_stream_pb2_grpc import VectorStreamStub


if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as channel, grpc.insecure_channel(
        "localhost:50051"
    ) as channel2:
        stub = VectorStreamStub(channel)
        stub2 = VectorStreamStub(channel2)
        ch1_response = stub.add_one(RequestResponse(data=[i]) for i in range(10))
        ch2_response = stub.add_one(RequestResponse(data=r.data) for r in ch1_response)
        for i, response in enumerate(ch2_response):
            print([i], response)
