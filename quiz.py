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
    "What is the functional unit of the kidney?": ["a) Nephron", "b) Alveoli", "c) Neuron", "a"],
    # this question is prepared by Eden Bogale
    "What is the basic unit of life?": ["a) Atom", "b) Cell", "c) Tissue", "b"],
    "Which particle has a negative charge?": ["a) Proton", "b) Neutron", "c) Electron", "c"],
    "What is the chemical symbol for water?": ["a) H2O", "b) O2", "c) CO2", "a"],
    "Which gas do plants absorb from the atmosphere?": ["a) Oxygen", "b) Nitrogen", "c) Carbon dioxide", "c"],
    "What is the pH of a neutral solution?": ["a) 0", "b) 7", "c) 14", "b"],
    "Which bond involves sharing electrons?": ["a) Ionic", "b) Covalent", "c) Metallic", "b"],
    "What is the center of an atom called?": ["a) Electron", "b) Nucleus", "c) Proton", "b"],
    "Which element is most abundant in the universe?": ["a) Oxygen", "b) Hydrogen", "c) Carbon", "b"],
    "What is the process of liquid turning into gas?": ["a) Condensation", "b) Evaporation", "c) Freezing", "b"],
    "Which state of matter has a definite volume but no fixed shape?": ["a) Solid", "b) Liquid", "c) Gas", "b"],
    "What is the smallest unit of a chemical element?": ["a) Molecule", "b) Atom", "c) Ion", "b"],
    "What type of bond forms between oppositely charged ions?": ["a) Covalent", "b) Ionic", "c) Hydrogen", "b"],
    "What is the number of protons in an atom called?": ["a) Mass number", "b) Atomic number", "c) Isotope", "b"],
    "Which subatomic particle is found outside the nucleus?": ["a) Proton", "b) Neutron", "c) Electron", "c"],
    "What is the formula for table salt?": ["a) NaCl", "b) KCl", "c) CaCl2", "a"],
    "Which element is a noble gas?": ["a) Oxygen", "b) Nitrogen", "c) Neon", "c"],
    "What is the process of a solid changing directly into a gas?": ["a) Sublimation", "b) Condensation", "c) Melting", "a"],
    "Which law states that matter cannot be created or destroyed?": ["a) Law of Conservation of Mass", "b) Boyle's Law", "c) Charles's Law", "a"],
    "What is the charge of a neutron?": ["a) Positive", "b) Negative", "c) Neutral", "c"],
    "Which element has the chemical symbol 'Fe'?": ["a) Fluorine", "b) Iron", "c) Francium", "b"],
    "What is the universal solvent?": ["a) Alcohol", "b) Water", "c) Acetone", "b"],
    "What is the term for a substance made of two or more elements chemically bonded?": ["a) Mixture", "b) Compound", "c) Solution", "b"],
    "Which type of reaction releases heat?": ["a) Endothermic", "b) Exothermic", "c) Neutralization", "b"],
    "What is the SI unit for amount of substance?": ["a) Mole", "b) Gram", "c) Liter", "a"],
    "What is Avogadro’s number?": ["a) 6.022×10²³", "b) 3.14", "c) 9.81", "a"]
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


# This part is done by EDEN
Q1  = """ 	Antonym of “optimistic”
A. 	Hopeful
B. 	Cheerful
C. 	Pessimistic
D. 	Confident"""
Q2 = """ Correct spelling
A. 	Recieve
B. 	Receive 
C. 	Receeve
D. 	Recive """
Q3 = """ 	Figure of speech: “The wind whispered through the trees.”
A. 	Simile
B. 	Metaphor
C. 	Personification 
D. 	Hyperbole"""
Q4 = """ 	Grammatically correct sentence
A. 	She don’t like coffee.
B. 	He go to school every day.
C. 	They has finished their homework.
D. 	I have never seen that movie. """

#🧬 Biology (4 Questions)
Q5 = """ 	Genetic material is found in the...
A. 	Cytoplasm
B. 	Nucleus 
C. 	Mitochondria
D. 	Ribosome""" 
Q6 = """ 	Function of white blood cells
A. 	Carry oxygen
B. 	Fight infection 
C. 	Digest food
D. 	Produce energy""" 
Q7 =	""" Organ that filters blood
A. 	Liver
B. 	Kidney 
C. 	Heart
D. 	Lungs"""
Q8 ="""	Photosynthesis occurs in...
A. 	Chloroplast 
B. 	Nucleus
C. 	Mitochondria
D. 	Golgi apparatus"""

#⚗️ Chemistry (4 Questions)
Q9 =""" 	Atomic number of oxygen
A. 	6
B. 	8 
C. 	10
D. 	12"""
Q10 = """	Noble gas among the following
A. 	Nitrogen
B. 	Oxygen
C. 	Argon 
D. 	Hydrogen"""
Q11 =""" 	Bond in NaCl
A. 	Covalent
B. 	Ionic 
C. 	Metallic
D. 	Hydrogen """
Q12 = """	pH of a basic solution
A. 	Less than 7
B. 	Equal to 7
C. 	Greater than 7 
D. 	Exactly 0 """

#🔭 Physics (4 Questions)
Q13 = """ 	Unit of force
A. 	Joule
B. 	Newton 
C. 	Watt
D. 	Pascal """
Q14 = """	Law of equal and opposite reaction
A. 	Newton’s First Law
B. 	Newton’s Second Law
C. 	Newton’s Third Law 
D. 	Law of Gravitation """
Q15 = """ 	Speed of sound in air (approx)
A. 	330 m/s 
B. 	3,000 m/s
C. 	30 m/s
D. 	1,000 m/s """
Q16 =""" 	Device converting electrical to mechanical energy
A. 	Generator
B. 	Transformer
C. 	Motor 
D. 	Battery"""

#🧮 Aptitude (4 Questions)
Q17 = """	Cost of 8 pens if 5 pens cost $20
A. 	$32 
B. 	$30
C. 	$25
D. 	$28 """
Q18 =""" 	Odd one out: 2, 4, 8, 16, 32, 65
A. 	2
B. 	4
C. 	65 
D. 	16 """
Q19 =""" 	Angle between clock hands at 3:15
A. 	0°
B. 	7.5° 
C. 	30°
D. 	45° """
Q20 =""" 	Shortest distance back: 3 km north, 4 km east
A. 	5 km 
B. 	7 km
C. 	1 km
D. 	6 km """

#➗ Mathematics (5 Questions)
Q21 =""" 	√144
A. 	10
B. 	11
C. 	12 
D. 	14 """
Q22 =""" 	Solve: 2x + 3 = 11
A. 	x = 3
B. 	x = 4 
C. 	x = 5
D. 	x = 6 """
Q23 =""" 	Area of triangle (base 10 cm, height 5 cm)
A. 	25 cm² 
B. 	50 cm²
C. 	15 cm²
D. 	30 cm²"""
Q24 = """ 	Next number: 1, 4, 9, 16, ?
A. 	20
B. 	25 
C. 	36
D. 	49 """
Q25 = """ 	Value of (3 + 2)²
A. 	25 
B. 	20
C. 	15
D. 	10 """


correct={Q1:'C',Q2:'B',Q3:'C',Q4:'D',Q5:'B'
        ,Q6:'B',Q7:'B',Q8:'A',Q9:'B',Q10:'C'
        ,Q11:'B',Q12:'C',Q13:'B',Q14:'C',Q15:'A'
        ,Q16:'C',Q17:'A',Q18:'C',Q19:'B',Q20:'A'
        ,Q21:'C',Q22:'B',Q23:'A',Q24:'B',Q25:'A'}
print("Welcome to General Quiz")
name = input("Enter your full name: ")
print(f"Dear {name}, Welcome to general quiz")
print("Please read  following instructions")
print("Instr. 1:any cancellation will loss your mark ")
print("Instr. 2: Cheating will disqualify your total result")
mark = 0
choice = ['a', 'b', 'c', 'd']
for item in correct:
    print(item)
    answer = input("Choose the correct answer a/b/c/d: ").upper()
   
    if answer==correct[item]:
        print(f" {answer} is correct answer, you got 2 pts.")
        mark = mark+2
    else:
        print(f"{answer} is incorrect, {correct[item]} is the correct answer")
        mark = mark
print(f"{mark}/60 ") 
