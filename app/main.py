from concurrent import futures
import grpc
from proto.generated_helper import storage_pb2_grpc

from app import PORT, APP_NAME


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # add health servicer to server and set it to be serving
    health_pb2_grpc.add_HealthServicer_to_server(HealthServicer(), server)
    HealthServicer().set('', health_pb2.HealthCheckResponse.SERVING)

    # add servicer to server
    storage_pb2_grpc.add_StorageServicer_to_server(
        StorageServicer(),
        server
    )

    # add port and start server
    port = server.add_insecure_port(f'[::]:{PORT}')
    server.start()
    logger.info(f"Started [{APP_NAME}] service on port {port}...")

    server.wait_for_termination()


if __name__ == "__main__":
    main()
