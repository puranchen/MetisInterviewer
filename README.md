# MetisInterviewer (MI)

MetisInterviewer (MI) is a chatbot specialized in medical consultations. MI conducts a structured interview with a simple text interface and is powered by clinical decision trees.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Structured Interviews**: Conducts structured medical interviews to gather comprehensive clinical information.
- **Clinical Decision Trees**: Uses clinical decision trees to guide the interview process and provide diagnostic/recommendation/decision support.
- **Integration with openEHR**: Structured clinical information using openEHR standards.
- **SNOMED Clinical Terms (SNOMED-CT)**: Leverages SNOMED-CT for standardized clinical terminology.
- **User-friendly Interface**: Simple text-based interface for ease of use.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/MetisInterviewer.git
    ```
2. Navigate to the project directory:
    ```sh
    cd MetisInterviewer
    ```
3. Install the necessary dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the chatbot, run:
```sh
python metis_interviewer.py
