import os
import shutil
from proto.generated_helper import storage_pb2_grpc
from proto.generated_helper.storage_pb2 import StoreMediaReq, StoreMediaRes, UploadStatus
from azure.storage.blob import BlobServiceClient
from app import AZURE_CONNECTION


class StorageServicer(storage_pb2_grpc.StorageServicer):
    """
        Store media files into Azure Cloud.

        Parameters
        ----------
        request : StoreReq
            A request object sent from the controller for storing of media.
    """

    # gRPC Request Method for storing of media files to cloud
    def StoreMedia(self, store_req: StoreReq, context):
        try:
            media_blob_name = f"{store_req.Metadata.uid}/{os.path.split(store_req.tmpPath)[-1]}"
            self.upload_media_to_azure(store_req.tmpPath, media_blob_name)

            # Updating media meta for controller
            store_req.mediaMeta.uploadStatus = UploadStatus.COMPLETED
              return StoreRes(
                mediaMeta=store_req.Metadata,
                uploadStatus="COMPLETED",
                statusCode="SUCCESS"
            )
        except Exception as e:
            return StoreRes(
                mediaMeta=store_req.Metadata,
                uploadStatus="FINAL_TRANSFER",
                statusCode="FAILED",
            )
        finally:
            shutil.rmtree(os.path.dirname(store_req.tmpPath), ignore_errors=True)

    # Method for media to be uploaded to Azure
    def upload_media_to_azure(self, file_path, blob_name):
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION)
        try:
            media_blob_client = blob_service_client.get_blob_client(
                container="container", blob=blob_name)
            # Upload media
            with open(file_path, "rb") as data:
                media_blob_client.upload_blob(data)
        except Exception as e:
            raise e
