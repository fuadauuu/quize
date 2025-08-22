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




print("Thank you Eden")




#This part is done by Melkam Eyosiyas 

import random
import time

questions = {
    "Which enzyme is responsible for unzipping the DNA helix during replication?":
        ["a) Ligase", "b) Helicase", "c) Polymerase", "d) Primase", "b", "Helicase unzips the DNA strands during replication."],
    "What is the main function of the Golgi apparatus?":
        ["a) Energy production", "b) Protein synthesis", "c) Packaging and transport of proteins", "d) DNA replication", "c", "The Golgi apparatus is responsible for packaging proteins and lipids for transport."],
    "Which phase of mitosis do chromosomes line up in the center of the cell?":
        ["a) Metaphase", "b) Anaphase", "c) Telophase", "d) Prophase", "a", "In Metaphase, chromosomes align at the cell's equatorial plane."],
    "In which organelle does the Krebs cycle take place?":
        ["a) Cytoplasm", "b) Mitochondria", "c) Nucleus", "d) Ribosome", "b", "The Krebs cycle occurs in the mitochondria, where energy is produced."],
    "Which molecule carries amino acids to ribosomes?":
        ["a) mRNA", "b) tRNA", "c) rRNA", "d) DNA", "b", "tRNA transports amino acids to the ribosome during protein synthesis."],
    "What is the name of the process by which plants lose water vapor through stomata?":
        ["a) Translocation", "b) Transpiration", "c) Evaporation", "d) Respiration", "b", "Transpiration is the process by which plants lose water vapor from their leaves through the stomata."],
    "Which part of the brain regulates body temperature?":
        ["a) Cerebrum", "b) Hypothalamus", "c) Cerebellum", "d) Medulla", "b", "The hypothalamus controls body temperature by regulating heat production and loss."],
    "Which genetic disorder is caused by an extra chromosome 21?":
        ["a) Turner syndrome", "b) Down syndrome", "c) Klinefelter syndrome", "d) Huntington's disease", "b", "Down syndrome is caused by an extra copy of chromosome 21."],
    "Which nitrogenous base is found only in RNA and not DNA?":
        ["a) Thymine", "b) Cytosine", "c) Uracil", "d) Adenine", "c", "Uracil is found in RNA and replaces thymine, which is present in DNA."],
    "What is the final electron acceptor in cellular respiration?":
        ["a) Carbon dioxide", "b) NAD+", "c) Oxygen", "d) FAD", "c", "Oxygen is the final electron acceptor in the electron transport chain during cellular respiration."],
    "Which type of muscle tissue is involuntary and found in the walls of internal organs?":
        ["a) Skeletal", "b) Cardiac", "c) Smooth", "d) Voluntary", "c", "Smooth muscle is found in the walls of organs and is involuntary."],
    "Which hormone regulates the sleep-wake cycle?":
        ["a) Insulin", "b) Melatonin", "c) Adrenaline", "d) Cortisol", "b", "Melatonin is produced by the pineal gland and regulates the sleep-wake cycle."],
    "Which macromolecule contains the most energy per gram?":
        ["a) Carbohydrates", "b) Proteins", "c) Lipids", "d) Nucleic acids", "c", "Lipids contain the most energy per gram, providing long-term energy storage."],
    "What structure connects the two hemispheres of the brain?":
        ["a) Cerebellum", "b) Corpus callosum", "c) Brainstem", "d) Medulla", "b", "The corpus callosum is the structure that connects the left and right hemispheres of the brain."],
    "What is the role of surfactant in the lungs?":
        ["a) Prevent infections", "b) Reduce surface tension", "c) Increase oxygen diffusion", "d) Absorb CO2", "b", "Surfactant reduces surface tension in the lungs, preventing alveolar collapse during exhalation."],
    "Which plant hormone is responsible for cell elongation?":
        ["a) Ethylene", "b) Cytokinin", "c) Auxin", "d) Gibberellin", "c", "Auxin promotes cell elongation, allowing the plant to grow towards light."],
    "Which organ is responsible for producing urea?":
        ["a) Liver", "b) Kidney", "c) Pancreas", "d) Spleen", "a", "The liver breaks down proteins and produces urea, which is then filtered by the kidneys."],
    "Which process converts nitrogen gas into a usable form for plants?":
        ["a) Denitrification", "b) Nitrogen fixation", "c) Nitrification", "d) Ammonification", "b", "Nitrogen fixation is the process by which nitrogen gas is converted into a form usable by plants."],
    "Which protein structure level is determined by hydrogen bonds in the backbone?":
        ["a) Primary", "b) Secondary", "c) Tertiary", "d) Quaternary", "b", "The secondary structure of a protein is formed by hydrogen bonds between the amino acid backbone."],
    "What type of immunity is achieved through vaccination?":
        ["a) Passive immunity", "b) Natural immunity", "c) Active artificial immunity", "d) Innate immunity", "c", "Active artificial immunity is acquired through vaccination, stimulating the immune system to recognize pathogens."],
    "Which structure prevents food from entering the windpipe?":
        ["a) Pharynx", "b) Epiglottis", "c) Larynx", "d) Esophagus", "b", "The epiglottis closes the windpipe during swallowing to prevent food from entering the lungs."],
    "Which part of the nephron is responsible for filtration?":
        ["a) Loop of Henle", "b) Glomerulus", "c) Collecting duct", "d) Bowman's capsule", "b", "The glomerulus is responsible for filtering blood to form urine."],
    "Which ion is essential for muscle contraction?":
        ["a) Sodium", "b) Potassium", "c) Calcium", "d) Magnesium", "c", "Calcium ions are released during muscle contraction and bind to troponin, triggering contraction."],
    "Which component of blood is responsible for clotting?":
        ["a) Plasma", "b) Platelets", "c) White blood cells", "d) Red blood cells", "b", "Platelets are responsible for blood clotting and wound repair."],
    "Which gas is most abundant in the Earth's atmosphere?":
        ["a) Oxygen", "b) Nitrogen", "c) Carbon dioxide", "d) Argon", "b", "Nitrogen makes up about 78% of Earth's atmosphere."],
    "Which type of RNA carries the genetic blueprint from the DNA to the ribosome?":
        ["a) mRNA", "b) tRNA", "c) rRNA", "d) miRNA", "a", "mRNA carries the genetic code from the DNA to the ribosome for protein synthesis."],
    "What is the primary function of the large intestine?":
        ["a) Absorption of nutrients", "b) Absorption of water", "c) Digestion of food", "d) Production of bile", "b", "The large intestine absorbs water and electrolytes, forming solid waste."],
    "What is the function of the ribosome in the cell?":
        ["a) Protein synthesis", "b) Energy production", "c) DNA replication", "d) Cell division", "a", "Ribosomes are the site of protein synthesis in the cell."],
    "What type of bond holds the two strands of DNA together?":
        ["a) Hydrogen bonds", "b) Ionic bonds", "c) Covalent bonds", "d) Peptide bonds", "a", "Hydrogen bonds hold the complementary base pairs in the two DNA strands together."],
    "Which of these organisms is capable of photosynthesis?":
        ["a) Fungi", "b) Plants", "c) Animals", "d) Bacteria", "b", "Plants are the primary organisms capable of photosynthesis, converting sunlight into chemical energy."],
    "What part of the chloroplast contains chlorophyll?":
        ["a) Thylakoid", "b) Stroma", "c) Outer membrane", "d) Inner membrane", "a", "Chlorophyll is located in the thylakoid membranes of the chloroplasts, where photosynthesis takes place."],
    "What is the genetic material found in viruses?":
        ["a) RNA", "b) DNA", "c) Both RNA and DNA", "d) Neither RNA nor DNA", "c", "Viruses can contain either RNA or DNA as their genetic material, not both."],
    "What type of bond links amino acids together in proteins?":
        ["a) Hydrogen bond", "b) Ionic bond", "c) Peptide bond", "d) Covalent bond", "c", "A peptide bond links amino acids to form proteins."],
}
print("Welcome to the Quiz Game!")
name=input("enter name")
print("dear ", name,"wellcome to quize")
print ("read carefully the following questions")
print(" cheating is not allowed")

def start_quiz():
    score = 0
    incorrect_questions = []
    start_time = time.time()

    
    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    for idx, question in enumerate(question_keys, 1):
        print(f"Question {idx}: {question}")
        options = questions[question][:4]
        correct_answer = questions[question][4]
        explanation = questions[question][5]
        
        
        for option in options:
            print(option)
        
        
        question_start_time = time.time()
        answer = input("Your answer (a/b/c/d): ").lower()
        question_end_time = time.time()

        
        time_taken = round(question_end_time - question_start_time, 2)
        
        if answer == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was '{correct_answer}'")
            incorrect_questions.append((question, correct_answer, explanation))

        print(f"⏱ You took {time_taken} seconds to answer.\n")

    total_time = round(time.time() - start_time, 2)
    print(f"🎯 Your final score is {score}/{len(questions)}")
    print(f"⏱ Total time taken: {total_time} seconds\n")
    
    
    if score >= 20:
        print("🌟 Excellent!")
    elif score >= 15:
        print("👍 Very good!")
    elif score <= 5:
        print("❌ You failed. Please review your biology notes.")
    else:
        print("📚 Keep practicing!")

    
    if incorrect_questions:
        print("\n📝 Review your incorrect answers:")
        for q, correct_answer, explanation in incorrect_questions:
            print(f"Question: {q}")
            print(f"Correct Answer: {correct_answer}")
            print(f"Explanation: {explanation}\n")

    print("🧠 Good luck and keep learning biology!")


if __name__ == "__main__":
    start_quiz()




# Developed by Hayat Hussen

quiz_hayat = {"What is the basic unit of life?": ["a) Atom", "b) Cell", "c) Tissue", "b"],
    "What is the capital of France?": ["a) Rome", "b) Madrid", "c) Paris", "c"],
    "Who wrote 'Romeo and Juliet'?": ["a) William Wordsworth", "b) William Shakespeare", "c) Charles Dickens", "b"],
    "Which planet is known as the Red Planet?": ["a) Mars", "b) Venus", "c) Jupiter", "a"],
    "What is H2O commonly known as?": ["a) Salt", "b) Water", "c) Hydrogen", "b"],
    "Which organ pumps blood in the human body?": ["a) Brain", "b) Liver", "c) Heart", "c"],
    "How many continents are there on Earth?": ["a) Five", "b) Seven", "c) Six", "b"],
    "What is the fastest land animal?": ["a) Lion", "b) Cheetah", "c) Horse", "b"],
    "Which is the smallest prime number?": ["a) 0", "b) 1", "c) 2", "c"],
    "Who invented the light bulb?": ["a) Nikola Tesla", "b) Albert Einstein", "c) Thomas Edison", "c"],
    "Which language is used to create web pages?": ["a) HTML", "b) Python", "c) C++", "a"],
    "Which is the largest planet in our solar system?": ["a) Saturn", "b) Earth", "c) Jupiter", "c"],
    "What is the boiling point of water?": ["a) 100°C", "b) 0°C", "c) 50°C", "a"],
    "Which animal is known as the king of the jungle?": ["a) Tiger", "b) Lion", "c) Elephant", "b"],
    "Which month has 28 or 29 days?": ["a) February", "b) January", "c) April", "a"],
    "Which part of the plant conducts photosynthesis?": ["a) Root", "b) Leaf", "c) Stem", "b"],
    "What is the main source of energy for Earth?": ["a) Wind", "b) Water", "c) Sun", "c"],
    "Which ocean is the largest?": ["a) Atlantic", "b) Pacific", "c) Indian", "b"],
    "What do bees produce?": ["a) Milk", "b) Honey", "c) Wax", "b"],
    "How many legs does a spider have?": ["a) 6", "b) 8", "c) 10", "b"],
    "Which planet is closest to the sun?": ["a) Earth", "b) Mercury", "c) Mars", "b"],
    "What is 10 × 10?": ["a) 100", "b) 10", "c) 20", "a"],
    "Which shape has three sides?": ["a) Square", "b) Circle", "c) Triangle", "c"],
    "What is the color of chlorophyll?": ["a) Red", "b) Green", "c) Blue", "b"]
}