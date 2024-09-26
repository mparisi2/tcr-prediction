from openai import OpenAI

class OpenAISession:

    def __init__(self, client:OpenAI, model:str = "gpt-4-turbo") -> None:
        self.client = client
        self.model = model

    def new_chat(self, prompt:str):
        messages = [{
                "role":"system",
                "content": """You are a parser. I want you to take in the COMPND section of a .pdb file and determine what the characters are that correspond to the T CELL RECEPTOR (TCR) ALPHA and BETA, the PEPTIDE or oncogene like KRAS or a string of amino acids, and the MHC or HLA CLASS I ANTIGEN (MHCI). If there are multiple characters in the chain section corresponding to each item: only consider the first chain. If a section does not exists then return NaN for that section. Your response should be exactly 4 comma seperated entries in the following order: TCRalpha,TCRbeta,Peptide,MHCI"""
            }, {
                "role":"user",
                "content":"""MOL_ID: 1;
        2 MOLECULE: MHC CLASS I ANTIGEN (FRAGMENT);
        3 CHAIN: A, D;
        4 ENGINEERED: YES;
        5 MUTATION: YES;
        6 MOL_ID: 2;
        7 MOLECULE: BETA-2-MICROGLOBULIN;
        8 CHAIN: B, E;
        9 FRAGMENT: UNP RESIDUES 21-119;
        10 ENGINEERED: YES;
        11 MOL_ID: 3;
        12 MOLECULE: VAL-ARG-SER-ARG-ARG-ABA-LEU-ARG-LEU;
        13 CHAIN: C, F;
        14 ENGINEERED: YES;
        15 MOL_ID: 4;
        16 MOLECULE: T CELL RECEPTOR ALPHA;
        17 CHAIN: G, I;
        18 ENGINEERED: YES;
        19 MOL_ID: 5;
        20 MOLECULE: T CELL RECEPTOR BETA;
        21 CHAIN: H, J;
        22 ENGINEERED: YES;
        23 MUTATION: YES"""
            }, {
                "role":"assistant",
                "content":"""G,H,C,A"""
            }, {
                "role":"user",
                "content": """MOL_ID: 1;
        2 MOLECULE: MHC CLASS I ANTIGEN (FRAGMENT);
        3 CHAIN: H;
        4 ENGINEERED: YES;
        5 MUTATION: YES;
        6 MOL_ID: 2;
        7 MOLECULE: BETA-2-MICROGLOBULIN;
        8 CHAIN: L;
        9 ENGINEERED: YES;
        10 MOL_ID: 3;
        11 MOLECULE: KRAS-G12WT-9;
        12 CHAIN: P;
        13 ENGINEERED: YES"""
            }, {
                "role":"assistant",
                "content":"NaN,NaN,P,H"
            }, {
                "role":"user",
                "content":prompt
            }]
        response = self.client.chat.completions.create(model = self.model, messages = messages, max_tokens=20)
        return response.choices[0].message.content