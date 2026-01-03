docker build --tag maya-stubs --target="build_stubs_stage" .
docker build --tag maya-stubs --target="mayapy_output_stage" --output="type=local,dest=." .
sudo chown -R $USER:$USER .cache
