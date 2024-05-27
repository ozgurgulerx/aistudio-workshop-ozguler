if __name__ == "__main__":
    from promptflow.tracing import start_trace

    start_trace()

    result = chat("What's the capital of France?")
    print(result)