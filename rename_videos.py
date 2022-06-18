# const hiddenElement = document.createElement('a')

# hiddenElement.href = 'data:attachment/json,' + encodeURI(JSON.stringify(Array.from(document.querySelectorAll("#video-title")).map(el => el.innerText)))
# hiddenElement.download = 'video_names.json'
# hiddenElement.click()

import os
# sample - TOC Neso Academy
# ordered_names = ["Introduction to Theory of Computation", "Finite State Machine (Prerequisites)", "Finite State Machine (Finite Automata)", "Deterministic Finite Automata (Example 1)", "Deterministic Finite Automata (Example 2)", "Deterministic Finite Automata (Example 3)", "Deterministic Finite Automata (Example 4)", "Regular Languages", "Operations on Regular Languages", "Non-Deterministic Finite Automata", "Formal Definition of Non-Deterministic Finite Automata (NFA)", "Non-Deterministic Finite Automata (Solved Example 1)", "Non-Deterministic Finite Automata (Solved Example 2)", "Non-Deterministic Finite Automata (Solved Example 3)", "Conversion of NFA to DFA", "Conversion of NFA to DFA (Example 1)", "Conversion of NFA to DFA (Example 2)", "Conversion of NFA to DFA (Example 3)", "Conversion of NFA to DFA (Example 4)", "Minimization of Deterministic Finite Automata (DFA)", "Minimization of DFA (Example 1)", "Minimization of DFA (Example 2)", "Minimization of DFA (With Multiple Final States)", "Minimization of DFA (With Unreachable States)", "Myhill Nerode Theorem - Table Filling Method", "Myhill Nerode Theorem - Table Filling Method (Example)", "Finite Automata With Outputs", "Construction of Mealy Machine", "Construction of Mealy Machine (Example 1)", "Construction of Mealy Machine (Example 2)", "Construction of Moore Machine", "Construction of Moore Machine (Example 1)", "Construction of Moore Machine (Example 2)", "Conversion of Moore Machine to Mealy Machine", "Conversion of Moore Machine to Mealy Machine (Example 1)", "Conversion of Moore Machine to Mealy Machine (Example 2)", "Conversion of Mealy Machine to Moore Machine", "Conversion of Mealy Machine to Moore Machine (Example 1)", "Conversion of Mealy Machine to Moore Machine (Example 2)", "Conversion of Mealy Machine to Moore Machine (Using Transition Table)", "Epsilon NFA", "Conversion of Epsilon NFA to NFA", "Conversion of Epsilon NFA to NFA - Examples (Part 1)", "Conversion of Epsilon NFA to NFA - Examples (Part 2)", "Regular Expression", "Regular Expression - Examples", "Identities of Regular Expression", "Arden’s Theorem", "An Example Proof using Identities of Regular Expressions", "Designing Regular Expressions", "NFA to Regular Expression Conversion", "DFA to Regular Expression Conversion", "DFA to Regular Expression Conversion (when the DFA has Multiple Final States)", "Conversion of Regular Expression to Finite Automata", "Conversion of Regular Expression to Finite Automata - Examples (Part 1)", "Conversion of Regular Expression to Finite Automata - Examples (Part 2)",
#                  "Conversion of Regular Expression to Finite Automata - Examples (Part 3)", "Equivalence of Two Finite Automata", "Equivalence of Two Finite Automata (Example)", "Pumping Lemma (For Regular Languages)", "Pumping Lemma (For Regular Languages) | Example 1", "Pumping Lemma (For Regular Languages) | Example 2", "Regular Grammar", "Derivations from a Grammar", "Context Free Grammar & Context Free Language", "Regular Languages & Finite Automata (Solved Problem 1)", "Regular Languages & Finite Automata (Solved Problem 2)", "Regular Languages & Finite Automata (Solved Problem 3)", "Regular Languages & Finite Automata (Solved Problem 4)", "Regular Languages & Finite Automata (Solved Problem 5)", "Regular Languages & Finite Automata (Solved Problem 6)", "Method to find whether a string belong to a Grammar or not", "Derivation Tree (Left & Right Derivation Trees)", "Ambiguous Grammar", "Simplification of CFG (Reduction of CFG)", "Simplification of CFG (Removal of Unit Productions)", "Simplification of CFG (Removal of Null Productions)", "Chomsky Normal Form & CFG to CNF Conversion", "Conversion of CFG to Chomsky Normal Form", "Greibach Normal Form & CFG to GNF Conversion", "CFG to GNF Conversion (Removal of Left Recursion)", "Pumping Lemma (For Context Free Languages)", "Pumping Lemma (For Context Free Languages) - Examples (Part 1)", "Pumping Lemma (For Context Free Languages) - Examples (Part 2)", "Pushdown Automata (Introduction)", "Pushdown Automata (Formal Definition)", "Pushdown Automata (Graphical Notation)", "Pushdown Automata Example (Even Palindrome) PART-1", "Pushdown Automata Example (Even Palindrome) PART-2", "Pushdown Automata Example (Even Palindrome) PART-3", "Equivalence of CFG and PDA (Part 1)", "Equivalence of CFG and PDA (Part 2a)", "Equivalence of CFG and PDA (Part 2b)", "Turing Machine - Introduction (Part 1)", "Turing Machine - Introduction (Part 2)", "Turing Machine (Formal Definition)", "Turing Machine (Example 1)", "Turing Machine (Example 2)", "The Church-Turing Thesis", "Turing Machine for Even Palindromes", "Turing Machine Programming Techniques (Part 1)", "Turing Machine Programming Techniques (Part 2)", "Turing Machine Programming Techniques (Part 3)", "Multitape Turing Machine", "Nondeterministic Turing Machine (Part 1)", "Nondeterministic Turing Machine (Part 2)", "Turing Machine as Problem Solvers", "Decidability and Undecidability", "Universal Turing Machine", "The Halting Problem", "Undecidability of the Halting Problem", "The Post Correspondence Problem", "Undecidability of the Post Correspondence Problem", "TOC – Conclusion and Summary"]

ordered_names = []

# custom function
for ordered_name in ordered_names:
    index = ordered_names.index(ordered_name)
    ordered_names[index] = ordered_name.replace("|", " ").replace(
        ":", "").replace("/", " ").replace("?", "")


# print(ordered_names)
# quit()


path = input('Enter absolute path to your videos folder - ')
path = fr'{path}'.format(path=path)

os.chdir(path=path)

for video_name in os.listdir():
    # print(ordered_names.index(video_name.replace(".mp4", ""))) # to check
    try:
        index = ordered_names.index(
            video_name.replace(".mp4", "").replace("    ", "   "))
        os.rename(video_name, f"{index}. {video_name}")
    except:
        if not video_name[:1].isnumeric():
            print(f'{video_name} not found in list (may be an unnecessary download)')
