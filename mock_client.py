import grpc
from proto.generated_helper import storage_pb2_grpc
from proto.generated_helper.storage_pb2 import StoreReq, Metadata
from app import PORT
from google.protobuf.empty_pb2 import Empty
from google.protobuf.json_format import MessageToDict, ParseDict

"""
The main callable function is run(). It creates a client stub that connects to 
the gRPC server. 
"""

CHUNK_SIZE = 1024 * 1024  # 1MB

def create_meta():
    mediameta = Metadata()
    mediameta.uid = 'test'
    mediameta.fullTitle = 'testsnfdj'
    mediameta.description = 'description dgdg'
    mediameta.fileSize = '3535'
    mediameta.mediaFormat = '480P'
    mediameta.uploadStatus = 2
    return mediameta

def call_storage_handler(stub):
    request = StoreReq(tmpPath='~/output/test/test.mp4',
                            mediaMeta=create_meta(),
                            tmpPath="~/test/output/test.png")
    response = stub.StoreMedia(request)
    return response

# def call_retrieve_file(stub):
#     request = FileId(id='60127ecb5532337102ca077c')
#     response = stub.RetrieveFile(request)
#     return response

# def call_retrieve_all(stub):
#     response = stub.retrieveAll(Empty())
#     return response

def run():
    channel = grpc.insecure_channel(f'localhost:{PORT}')
    stub = storage_pb2_grpc.StorageStub(channel)

    response = call_storage_handler(stub)
    print(response)

run()
