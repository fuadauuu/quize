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
    "Who among the following coined the term 'cell'?":
        ["a) Theodor Schwann", "b) Robert Hooke", "c) Oswald Avery", "d) Gerhard Domagk", "b", "Robert Hooke coined the term 'cell'."],
    "The suicidal bags of the cell are:":
        ["a) Lysosomes", "b) Ribosomes", "c) Dictyosomes", "d) Phagosomes", "a", "Lysosomes are known as the 'suicidal bags' of the cell."],
    "In which part of the cell are proteins made?":
        ["a) Reticulum", "b) Golgi apparatus", "c) Ribosomes", "d) Lysosome", "c", "Proteins are synthesized in ribosomes."],
    "Name the scientist who proposed the cell theory.":
        ["a) Schleiden and Schwann", "b) Lamarck", "c) Treviranus", "d) Whittaker and Stanley", "a", "Schleiden and Schwann proposed the cell theory."],
    "Which cell organelle is also called the 'power house of a cell'?":
        ["a) Lysosome", "b) Mitochondria", "c) Golgi Apparatus", "d) Plastids", "b", "Mitochondria generate cellular energy, thus 'power house'."],
    "The cell wall of a plant is composed of:":
        ["a) Lipoprotein", "b) Carbohydrates", "c) Cellulose", "d) Lipids", "c", "Cellulose is the main component of the plant cell wall."],
    "What is contained in Chlorophyll?":
        ["a) Sodium", "b) Potassium", "c) Manganese", "d) Magnesium", "d", "Magnesium is the central atom in chlorophyll."],
    "Which part of a plant cell traps sunlight to make sugar?":
        ["a) Chloroplast", "b) Leucoplast", "c) Chromoplast", "d) Starch grain", "a", "Chloroplasts capture light for photosynthesis."],
    "Which of the following is not connective tissue?":
        ["a) Bone", "b) Cartilage", "c) Blood", "d) Skeletal muscle", "d", "Skeletal muscle is not connective tissue."],
    "Skeletal muscles are attached to the skeleton by tough connective tissues called:":
        ["a) Cartilage", "b) Neurons", "c) Ligament", "d) Tendons", "d", "Tendons connect muscles to bones."],
    "In plants, water is transported through which of the following medium?":
        ["a) Xylem", "b) Phloem", "c) Stomata", "d) Root hair", "a", "Xylem transports water in plants."],
    "Name the tissue that transports food to various parts of a plant.":
        ["a) Phloem", "b) Xylem", "c) Parenchyma", "d) Sclerenchyma", "a", "Phloem distributes food in plants."],
    "What does RNA stand for?":
        ["a) Rado Nuclear Acid", "b) Ribo Nucleic Acid", "c) Rhino Nuclear Acid", "d) Resto Nucleus Acid", "b", "RNA stands for Ribo Nucleic Acid."],
    "DNA stands for:":
        ["a) Di Nucleic Acid", "b) Deoxy Nucleic Acid", "c) Di ribonucleic Acid", "d) Deoxyribonucleic Acid", "d", "DNA stands for Deoxyribonucleic Acid."],
    "What is the basic unit of heredity?":
        ["a) DNA", "b) RNA", "c) Chromosome", "d) Gene", "d", "A gene is the basic unit of heredity."],
    "Which food component has the highest gross calorific value?":
        ["a) Proteins", "b) Fats", "c) Carbohydrates", "d) Vitamins", "b", "Fats provide the highest calories per gram."],
    "Which of the following has the highest protein content per gram?":
        ["a) Apple", "b) Soyabean", "c) Wheat", "d) Groundnut", "b", "Soybeans are richer in protein per gram."],
    "Which of the following is an active enzyme?":
        ["a) trypsin", "b) trypsinogen", "c) chymotrypsinogen", "d) procarboxypeptidases", "a", "Trypsin is an active protein‑digesting enzyme."],
    "In which form are carbohydrates stored in our body?":
        ["a) Lactose", "b) Cellulose", "c) Glycogen", "d) Glucose", "c", "Carbohydrates are stored as glycogen."],
    "Enzyme in the human body that breaks down carbohydrates is:":
        ["a) Protease", "b) Lipase", "c) Pepsin", "d) Amylase", "d", "Amylase catalyzes carbohydrate digestion."],
    "Which chromosome combination results in a female?" :
        ["a) ZX", "b) XX", "c) YZ", "d) XY", "b", "XX is the female chromosome combination."],
    "How many chromosomes does a human cell contain?":
        ["a) 6", "b) 26", "c) 46", "d) 66", "c", "Human somatic cells have 46 chromosomes."],
    "Mendel is known as the:":
        ["a) Father of Physiology", "b) Father of Geology", "c) Father of Genetics", "d) Father of Biology", "c", "Mendel is regarded as the Father of Genetics."],
    "Charles Darwin proposed his theory in which book?":
        ["a) The families of flowering plant", "b) The origin of species", "c) The life on earth", "d) The story of the living world", "b", "Darwin's theory appears in 'The Origin of Species'."],
    "Binomial Nomenclature was founded by:":
        ["a) Charles Darwin", "b) Robert Nucleus", "c) Carl Linnaeus", "d) Lamarck", "c", "Carl Linnaeus developed binomial nomenclature."],
    "Five-kingdom classification was proposed by:":
        ["a) Whittaker", "b) Huxley", "c) Linnaeus", "d) Lamarck", "a", "Whittaker proposed the five-kingdom system."],
    "Amoeba belongs to which kingdom?":
        ["a) Monera", "b) Fungi", "c) Protista", "d) Animalia", "c", "Amoeba is classified under Protista."],
    "Which organism is considered both living and non-living?":
        ["a) Bacteria", "b) Fungi", "c) Algae", "d) Virus", "d", "Viruses lie at the boundary of living and non-living."],
    "Which organism belongs to Monera?":
        ["a) Bacteria", "b) Mushroom", "c) Fungi", "d) Bread mould", "a", "Bacteria are part of Monera."],
    "Sponges belong to which phylum?":
        ["a) Protozoa", "b) Annelida", "c) Porifera", "d) Cnidaria", "c", "Sponges are in the phylum Porifera."],
    "Which type of reproduction occurs in Hydra?":
        ["a) Fragmentation", "b) Budding", "c) Binary Fission", "d) Spore Formation", "b", "Hydra reproduces via budding."],
    "Earthworms belong to the phylum:":
        ["a) Protozoa", "b) Cnidaria", "c) Annelida", "d) Mollusca", "c", "Earthworms are annelids."],
    "Which of the following is an Arthropod?":
        ["a) Blood sucking leech", "b) Hookworm", "c) Earthworm", "d) Scorpion", "d", "Scorpion is an arthropod."],
    "Which has an open vascular system?":
        ["a) Cockroach", "b) Human", "c) Rat", "d) Birds", "a", "Cockroaches have an open circulatory system."],
    "Crocodiles have how many heart chambers?":
        ["a) Three", "b) One", "c) Four", "d) Two", "c", "Crocodiles possess a four-chambered heart."],
    "Which term describes the lowest member of the food chain?":
        ["a) Producer", "b) Digester", "c) Primary", "d) Herbivore", "a", "Producers form the base of food chains."],
    "Domain, Kingdom and Phylum are examples of what?":
        ["a) Class", "b) Classification level", "c) Taxonomic rank", "d) Biological classification", "c", "They are taxonomic ranks."],
    "Who first described classical conditioning?":
        ["a) Dmitri Mendeleev", "b) Ivan Pavlov", "c) Mikhail Lomonosov", "d) Ignaz Semmelweis", "b", "Ivan Pavlov introduced classical conditioning."],
    "Ornithology is the study of what?":
        ["a) Fish", "b) Birds", "c) Reptiles", "d) Amphibians", "b", "Ornithology is the study of birds."],
    "Why are viruses considered non-living by many biologists?":
        ["a) Not sentient", "b) Don't need food", "c) Don't excrete", "d) Can't reproduce without a host", "d", "Viruses can't reproduce without a host."],
    "Which fish is poisonous?":
        ["a) Surgeonfish", "b) Piranha", "c) Stonefish", "d) Grouper", "c", "Stonefish are poisonous."],
    "What is the common name for Notamacropus?":
        ["a) Possum", "b) Skunk", "c) Bobcat", "d) Wallaby", "d", "Notamacropus refers to wallabies."],
    "Which disease is caused by bacterial infection?":
        ["a) Chickenpox", "b) Giardia", "c) Lyme Disease", "d) Cystic fibrosis", "c", "Lyme disease is bacterial."],
    "Animals probably evolved from:":
        ["a) plants", "b) protists", "c) fungi", "d) lichens", "b", "Animals likely evolved from protists."],
    "Which animal is radially symmetrical?":
        ["a) Flatworm", "b) Jellyfish", "c) Roundworm", "d) Lobster", "b", "Jellyfish exhibit radial symmetry."],
    "Segmented animals with exoskeletons are called?":
        ["a) Platyhelminthes", "b) Molluscs", "c) Annelida", "d) Arthropods", "d", "These are arthropods."],
    "A water‑filled plant cell is ___, while one that loses water is ___.":
        ["a) lysed, not lysed", "b) lysed, flaccid", "c) turgid, flaccid", "d) flaccid, turgid", "c", "Turgid vs flaccid describes water status."],
    "The four major classes of biological molecules include:":
        ["a) organics...", "b) carbohydrates, saccharides...", "c) carbs, lipids, proteins, amino acids", "d) carbs, lipids, proteins, nucleic acids", "d", "The four macromolecule classes."],
    "Fundamental unit of fungal structure is:":
        ["a) spores", "b) gametes", "c) the hypha", "d) the mycelium", "d", "The mycelium is the fungal body."],

        "What is the primary pigment used in photosynthesis?":
        ["a) Chlorophyll", "b) Melanin", "c) Hemoglobin", "d) Myoglobin", "a", "Chlorophyll absorbs sunlight to drive the process of photosynthesis."],
    "Which part of the brain is responsible for balance and coordination?":
        ["a) Cerebrum", "b) Hypothalamus", "c) Medulla", "d) Cerebellum", "d", "The cerebellum manages balance, coordination, and posture."],
    "Which gas is produced during photosynthesis?":
        ["a) Carbon dioxide", "b) Oxygen", "c) Nitrogen", "d) Methane", "b", "Photosynthesis produces oxygen as a by-product."],
    "What is the smallest blood vessel in the human body?":
        ["a) Artery", "b) Vein", "c) Capillary", "d) Venule", "c", "Capillaries are the smallest blood vessels where gas exchange occurs."],
    "Which blood cells help fight infection?":
        ["a) Red blood cells", "b) Platelets", "c) Plasma cells", "d) White blood cells", "d", "White blood cells defend the body against pathogens."],
    "Which organ stores bile?":
        ["a) Liver", "b) Gallbladder", "c) Pancreas", "d) Small intestine", "b", "The gallbladder stores bile produced by the liver."],
    "Which human system includes the skin?":
        ["a) Nervous system", "b) Respiratory system", "c) Integumentary system", "d) Circulatory system", "c", "The integumentary system includes the skin, hair, and nails."],
    "What do lysosomes contain?":
        ["a) Enzymes", "b) RNA", "c) Ribosomes", "d) Mitochondria", "a", "Lysosomes contain digestive enzymes that break down waste."],
    "Which part of the plant conducts water?":
        ["a) Phloem", "b) Xylem", "c) Stomata", "d) Chloroplast", "b", "Xylem conducts water from roots to the rest of the plant."],
    "Which is a non-cellular infectious agent?":
        ["a) Bacteria", "b) Fungi", "c) Virus", "d) Protozoa", "c", "Viruses are acellular and need a host to reproduce."],
    "What is the main function of DNA?":
        ["a) Provide energy", "b) Transport oxygen", "c) Store genetic information", "d) Fight infections", "c", "DNA carries genetic information for development and function."],
    "What part of the brain controls breathing?":
        ["a) Cerebrum", "b) Cerebellum", "c) Medulla oblongata", "d) Hypothalamus", "c", "The medulla oblongata regulates involuntary actions like breathing."],
    "What type of reproduction creates genetically identical offspring?":
        ["a) Asexual reproduction", "b) Sexual reproduction", "c) Cross-pollination", "d) Fertilization", "a", "Asexual reproduction produces clones of the parent organism."],
    "Which blood type is a universal donor?":
        ["a) AB+", "b) A-", "c) O-", "d) B+", "c", "O-negative blood can be given to anyone in emergencies."],
    "What do mitochondria produce?":
        ["a) Proteins", "b) ATP", "c) DNA", "d) Hormones", "b", "Mitochondria are the site of ATP (energy) production."],
    "Which of the following is an autotroph?":
        ["a) Lion", "b) Fungus", "c) Tree", "d) Human", "c", "Autotrophs like trees produce their own food via photosynthesis."],
    "What is the basic structure of proteins?":
        ["a) Nucleotides", "b) Fatty acids", "c) Monosaccharides", "d) Amino acids", "d", "Proteins are composed of amino acids linked by peptide bonds."],
    "What is the main excretory organ in humans?":
        ["a) Liver", "b) Kidney", "c) Lungs", "d) Skin", "b", "The kidneys filter waste from the blood to form urine."],
    "Which structure regulates the amount of light entering the eye?":
        ["a) Retina", "b) Cornea", "c) Iris", "d) Lens", "c", "The iris adjusts the pupil to regulate light entry."],
    "Which system transports nutrients and oxygen to cells?":
        ["a) Digestive", "b) Nervous", "c) Circulatory", "d) Excretory", "c", "The circulatory system delivers oxygen and nutrients throughout the body."]

}
                
                
        #This part is done by Eyosiyas  


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



          # This part is done by Fuad



    import random

for question, data in questions.items():
    options = data[:4]
    correct_answer = data[4]
    explanation = data[5]

    print(question)
    for option in options:
        print(option)
    user_answer = input("Your answer (a/b/c/d): ").lower()
    
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! Correct answer is {correct_answer}) {options[ord(correct_answer)-97][3:]}")
    print("Explanation:", explanation)
    print("-" * 40)




          #This part is done by Banchayehu



    import random

question = random.choice(list(questions.keys()))
options = questions[question][:4]
correct_answer = questions[question][4]
explanation = questions[question][5]

print(question)
for option in options:
    print(option)
user_answer = input("Your answer (a/b/c/d): ").lower()

if user_answer == correct_answer:
    print("Correct!")
else:
    print(f"Wrong! The correct answer is {correct_answer}) {options[ord(correct_answer) - 97][3:]}")
print("Explanation:", explanation)



            #This part is done by Eden



import random

score = 0
questions_sample = random.sample(list(questions.items()), 5)

for question, data in questions_sample:
    options = data[:4]
    correct_answer = data[4]
    explanation = data[5]

    print(question)
    for option in options:
        print(option)
    user_answer = input("Your answer (a/b/c/d): ").lower()

    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}) {options[ord(correct_answer) - 97][3:]}")
    print("Explanation:", explanation)
    print()

print(f"Your final score: {score} out of 5")



             #This part is done by hayat husen


import random

for question, data in questions.items():
    options = data[:4]
    correct_answer = data[4]
    explanation = data[5]

    print(question)
    for option in options:
        print(option)
    
    while True:
        user_answer = input("Your answer (a/b/c/d): ").lower()
        if user_answer == correct_answer:
            print("Correct!")
            break
        else:
            print(f"Wrong! Try again.")
    print("Explanation:", explanation)
    print("-" * 40)
