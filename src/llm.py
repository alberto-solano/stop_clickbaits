import together


def togetherai_inference(
    prompt,
    **kwargs,
):
    model = kwargs.get("model")
    max_tokens = kwargs.get("max_tokens")
    temperature = kwargs.get("temperature")
    top_p = kwargs.get("top_p")
    top_k = kwargs.get("top_k")
    repetition_penalty = kwargs.get("repetition_penalty")

    output = together.Complete.create(
        prompt=prompt,
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
    )

    model_out = output["output"]["choices"][0]["text"]

    return model_out
