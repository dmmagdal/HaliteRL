#!/bin/bash

cp fluorine-dockerfile ../fluorine
cd ../fluorine/
docker build -t flourine -f fluorine-dockerfile .
rm fluorine-dockerfile
cd ../ReplayDockerfiles