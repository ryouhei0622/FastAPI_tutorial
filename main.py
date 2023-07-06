from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    example = "sairiumu"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# print(ModelName.alexnet.value)
# a = ModelName("alexnet")
# print(a is ModelName.alexnet)

print(ModelName["example"])
print(ModelName["example"].value)
print(ModelName.example)
print(ModelName.example.value)
print(ModelName("sairiumu"))
print(ModelName("sairiumu").value)
