for filename in ./proto/*
do
  key="$(echo "$filename" | sed -e 's#^./proto/##; s#.proto$##')"
  if [ $key = "generated_helper" ]
  then
    continue
  else
    mkdir -p ./proto/generated_helper
    # python code generation
    python -m grpc_tools.protoc \
        -I=./proto \
        --python_out=./proto/generated_helper/ \
        --grpc_python_out=./proto/generated_helper/ \
        $filename
    pb_grpc_file=${key}_pb2_grpc.py
    sed -i 's/import '$key'_pb2/from proto.generated_helper import '$key'_pb2/g ' ./proto/generated_helper/${pb_grpc_file}
  fi
done