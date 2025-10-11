import tensorflow as tf

try:
    gpu_devices = tf.config.list_physical_devices('GPU')
    print(f"TensorFlow Version: {tf.__version__}")
    print(f"Num GPUs Available: {len(gpu_devices)}")

    if gpu_devices:
        print("\n--- GPU Details ---")
        for device in gpu_devices:
            print(device)
        print("\nCongratulations, your GPU is detected and ready to use! ✅")
    else:
        print("\nGPU not detected. Please check your installation steps. ❌")

except Exception as e:
    print(f"An error occurred: {e}")