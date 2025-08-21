questions = {
    "What is the basic unit of life?": ["a) Atom", "b) Cell", "c) Tissue", "b"],
    "Which organelle is known as the powerhouse of the cell?": ["a) Ribosome", "b) Mitochondria", "c) Nucleus", "b"],
    "Which pigment is responsible for photosynthesis?": ["a) Hemoglobin", "b) Chlorophyll", "c) Carotene", "b"],
    "What is the genetic material in most organisms?": ["a) DNA", "b) RNA", "c) Protein", "a"],
    "Which kingdom includes mushrooms?": ["a) Plantae", "b) Fungi", "c) Protista", "b"],
    "What part of the plant conducts photosynthesis?": ["a) Root", "b) Stem", "c) Leaf", "c"],
    "Which blood cells help fight infections?": ["a) Red blood cells", "b) White blood cells", "c) Platelets", "b"],
    "Which part of the cell controls activities?": ["a) Nucleus", "b) Cytoplasm", "c) Ribosome", "a"],
    "What is the largest organ in the human body?": ["a) Brain", "b) Skin", "c) Liver", "b"],
    "Which vitamin is produced in the skin with sunlight?": ["a) Vitamin C", "b) Vitamin D", "c) Vitamin B12", "b"],
    "Which organ purifies blood in humans?": ["a) Kidney", "b) Heart", "c) Lungs", "a"],
    "Which process produces gametes?": ["a) Mitosis", "b) Meiosis", "c) Fertilization", "b"],
    "Which blood group is the universal donor?": ["a) AB", "b) O", "c) A", "b"],
    "Which blood group is the universal recipient?": ["a) AB", "b) O", "c) B", "a"],
    "Which organ is responsible for pumping blood?": ["a) Lungs", "b) Heart", "c) Kidney", "b"],
    "Which tissue connects bones to muscles?": ["a) Ligament", "b) Tendon", "c) Cartilage", "b"],
    "What type of blood cells carry oxygen?": ["a) Platelets", "b) Red blood cells", "c) White blood cells", "b"],
    "Which gas do humans exhale?": ["a) Oxygen", "b) Carbon dioxide", "c) Nitrogen", "b"],
    "Which organ is responsible for detoxification?": ["a) Stomach", "b) Liver", "c) Pancreas", "b"],
    "What is the hardest substance in the human body?": ["a) Bone", "b) Enamel", "c) Cartilage", "b"],
    "Which part of the brain controls balance?": ["a) Cerebrum", "b) Cerebellum", "c) Medulla", "b"],
    "Which blood vessels carry blood to the heart?": ["a) Arteries", "b) Veins", "c) Capillaries", "b"],
    "What is the main organ of the respiratory system?": ["a) Lungs", "b) Heart", "c) Kidney", "a"],
    "Which organ stores bile?": ["a) Pancreas", "b) Gallbladder", "c) Liver", "b"],
    "What is the functional unit of the kidney?": ["a) Nephron", "b) Alveoli", "c) Neuron", "a"]
}
score = 0

print("Welcome to the Quiz Game!")
name=input("enter name")
print("dear ", name,"wellcome to quize")
print ("read carefully the following questions")
print(" cheating is not allowed")
for question, options in questions.items():
    print(question)
    for option in options[:-1]:  # Display choices
        print(option)
    answer = input("Your answer: ").lower()

    if answer == options[-1]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was '{options[-1]}'\n")
print(f" Your final score is {score}/{len(questions)}")# Simple Quiz Game
if score>=20:
        print("excellent")
elif score >=15:
        print("very good")
elif score <=5:
        print (" you are failed")
print("good luck")
print("Eyosias part")
