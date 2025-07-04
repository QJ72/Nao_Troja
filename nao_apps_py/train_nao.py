from nao_classes.NaoTrainer import NaoTrainer

def main():
    trainer = NaoTrainer(dataset_name="dataset2")
    trainer.load_data()
    trainer.set_model_name("dummy_model.pth")
    model = trainer.create_model()
    print("Starting training...")
    train_losses, val_losses = trainer.train(epochs=50)

    print("\nEvaluating model...")
    trainer.evaluate_model()


if __name__ == "__main__":
    main()