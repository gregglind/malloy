# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from services.v1 import compiler_pb2 as services_dot_v1_dot_compiler__pb2


class CompilerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Compile = channel.unary_unary(
                '/malloy.services.v1.Compiler/Compile',
                request_serializer=services_dot_v1_dot_compiler__pb2.CompileRequest.SerializeToString,
                response_deserializer=services_dot_v1_dot_compiler__pb2.CompileResponse.FromString,
                )
        self.CompileStream = channel.stream_stream(
                '/malloy.services.v1.Compiler/CompileStream',
                request_serializer=services_dot_v1_dot_compiler__pb2.CompileRequest.SerializeToString,
                response_deserializer=services_dot_v1_dot_compiler__pb2.CompilerRequest.FromString,
                )


class CompilerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Compile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompileStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CompilerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Compile': grpc.unary_unary_rpc_method_handler(
                    servicer.Compile,
                    request_deserializer=services_dot_v1_dot_compiler__pb2.CompileRequest.FromString,
                    response_serializer=services_dot_v1_dot_compiler__pb2.CompileResponse.SerializeToString,
            ),
            'CompileStream': grpc.stream_stream_rpc_method_handler(
                    servicer.CompileStream,
                    request_deserializer=services_dot_v1_dot_compiler__pb2.CompileRequest.FromString,
                    response_serializer=services_dot_v1_dot_compiler__pb2.CompilerRequest.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'malloy.services.v1.Compiler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Compiler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Compile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/malloy.services.v1.Compiler/Compile',
            services_dot_v1_dot_compiler__pb2.CompileRequest.SerializeToString,
            services_dot_v1_dot_compiler__pb2.CompileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompileStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/malloy.services.v1.Compiler/CompileStream',
            services_dot_v1_dot_compiler__pb2.CompileRequest.SerializeToString,
            services_dot_v1_dot_compiler__pb2.CompilerRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
