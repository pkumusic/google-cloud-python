# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.automl_v1.proto import (
    prediction_service_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_prediction__service__pb2,
)


class PredictionServiceStub(object):
    """AutoML Prediction API.

  On any input that is documented to expect a string parameter in
  snake_case or kebab-case, either of those cases is accepted.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.Predict = channel.unary_unary(
            "/google.cloud.automl.v1.PredictionService/Predict",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_prediction__service__pb2.PredictRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_prediction__service__pb2.PredictResponse.FromString,
        )


class PredictionServiceServicer(object):
    """AutoML Prediction API.

  On any input that is documented to expect a string parameter in
  snake_case or kebab-case, either of those cases is accepted.
  """

    def Predict(self, request, context):
        """Perform an online prediction. The prediction result will be directly
    returned in the response.
    Available for following ML problems, and their expected request payloads:
    * Translation - TextSnippet, content up to 25,000 characters, UTF-8
    encoded.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PredictionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Predict": grpc.unary_unary_rpc_method_handler(
            servicer.Predict,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_prediction__service__pb2.PredictRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_prediction__service__pb2.PredictResponse.SerializeToString,
        )
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.automl.v1.PredictionService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
