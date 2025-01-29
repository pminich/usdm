1. **Install** `@openapitools/openapi-generator-cli`: If you haven’t yet installed it as a dependency, make sure it's in your project with the following command:
``` bash
   npm install @openapitools/openapi-generator-cli --save-dev
```
1. **Run the Command**: Use the following command to generate only the models:
``` bash
   npx @openapitools/openapi-generator-cli generate \
    -i <YOUR_OPENAPI_SPEC>.yaml \
    -g python \
    --enable-post-process-file \
    --global-property models
```
- `-i <YOUR_OPENAPI_SPEC>.yaml`: Replace `<YOUR_OPENAPI_SPEC>` with the path or URL to your OpenAPI specification file.
- `-g python`: This specifies the generator type (`python` for Python code).
- `--global-property models`: This option ensures that only the models are generated.
- `--enable-post-process-file` (optional): Allows post-processing if required by your project setup.

1. **Output Folder**: By default, the output is generated in a folder named `generated-code/<name-of-generator>` (e.g., `generated-code/python`). If you want to specify a custom folder for the output, add the `-o` option:
``` bash
   -o <TARGET_DIRECTORY>
```
Replace `<TARGET_DIRECTORY>` with the path to your desired output directory.
### Example Command:
``` bash
npx @openapitools/openapi-generator-cli generate \
  -i ./openapi-spec.yaml \
  -g python \
  --global-property models \
  -o ./python-models
```
This command will generate only the Python models and save them in the `./python-models` folder.


openapi-generator-cli generate -i .\USDM_API.yaml -g python --global-property models -o .\python-models --skip-validate-spec
openapi-generator-cli generate -i .\USDM_API.yaml -g typescript --global-property models -o .\ts-models --skip-validate-spec
openapi-generator-cli generate -i .\USDM_API.yaml -g python-pydantic-v1 --global-property models -o .\python-pydantic-v1-models --skip-validate-spec

openapi-generator-cli generate -i .\src\USDM-Model_openapi.yaml -g python-pydantic-v1 --global-property models -o .\datastructure-python-pydantic-v1-models --skip-validate-spec