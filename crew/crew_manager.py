import os
from tools.yf_tech_analysis_tool import perform_technical_analysis
from tools.yf_fundamental_analysis_tool import perform_fundamental_analysis

def create_crew(stock_symbol, model_option):
    # Perform fundamental and technical analysis
    fundamental_analysis = perform_fundamental_analysis(stock_symbol)
    technical_analysis = perform_technical_analysis(stock_symbol)

    # Ensure the results are dictionaries; handle errors
    results = {
        "Fundamental Analysis": fundamental_analysis
        if isinstance(fundamental_analysis, dict) else {"Error": fundamental_analysis},
        "Technical Analysis": technical_analysis
        if isinstance(technical_analysis, dict) else {"Error": technical_analysis},
    }

    # Save results to a file
    file_path = f"./data/outputs/{stock_symbol}_analysis.txt"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        for section, data in results.items():
            file.write(f"{section}:\n")
            for key, value in data.items():
                file.write(f"- {key}: {value}\n")
            file.write("\n")
    
    return file_path
