# Idea Synthesis and Extraction Engine (ISEE)

## Project Overview

The Idea Synthesis and Extraction Engine is a meta-framework for innovation that systematically leverages AI to generate, evaluate, and extract high-value concepts across any domain. Rather than using AI in a single-prompt manner, this framework creates a deliberate combinatorial approach that maximizes the exploration of possibility space before filtering for the most promising ideas.

## Repository Contents

This repository contains the following files:

- `README.md` - This file providing an overview of the project
- `main.py` - The main application for running the ISEE pipeline
- `model_api_integration.py` - Module for integrating with AI model APIs
- `instruction_templates.py` - Module for managing instruction templates
- `query_generator.py` - Module for generating query variations
- `domain_manager.py` - Module for managing application domains
- `evaluation_scoring.py` - Module for evaluating and scoring generated ideas
- `sample_config.json` - Sample configuration file
- `requirements.txt` - Package dependencies
- `workflow_diagram.svg` - Visual representation of the ISEE system architecture
- `implementation_guide.md` - Guide for implementing the ISEE framework

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up API keys for the models you want to use:
   - For Claude: Set the `ANTHROPIC_API_KEY` environment variable
   - For OpenAI: Set the `OPENAI_API_KEY` environment variable

## Usage

### Basic Usage

Run the complete pipeline with a single query:

```bash
python main.py --query "How might we improve urban transportation in the next decade?" --domain "Urban Planning" --max-combinations 10
```

This will:
1. Create a new query based on the input text
2. Generate variations of the query
3. Generate combinations of models, instructions, queries, and domains
4. Execute the combinations (using real API calls if API keys are available)
5. Evaluate the results
6. Synthesize ideas from the top results
7. Format and display the output

### API Integration

The system now supports real API calls to Anthropic (Claude) and OpenAI models. To use this functionality:

1. Set up API keys by either:

   **Option 1:** Using environment variables:
   ```bash
   # For Anthropic Claude models
   export ANTHROPIC_API_KEY=your_api_key_here
   
   # For OpenAI GPT models
   export OPENAI_API_KEY=your_api_key_here
   ```
   
   **Option 2:** Using a .env file (recommended for development):
   ```bash
   # Copy the template file
   cp .env.template .env
   
   # Edit the .env file with your API keys
   nano .env  # or use any text editor
   ```

2. Configure models in a configuration file (see `sample_config.json` for an example)

3. Run with the config file:
   ```bash
   python main.py --config sample_config.json --query "Your query here"
   ```

You can force simulation mode even if API keys are available by using the `--simulate` flag.

### Command-Line Options

```
usage: main.py [-h] [--config CONFIG] [--save-state SAVE_STATE] [--load-state LOAD_STATE] [--query QUERY] [--domain DOMAIN] 
               [--models MODELS] [--instructions INSTRUCTIONS] [--variations VARIATIONS] [--max-combinations MAX_COMBINATIONS]
               [--output-format {markdown,json}] [--output-file OUTPUT_FILE] [--simulate] [--dry-run]

Idea Synthesis and Extraction Engine

options:
  -h, --help            show this help message and exit
  --config CONFIG       Path to configuration file
  --save-state SAVE_STATE
                        Save application state to file
  --load-state LOAD_STATE
                        Load application state from file
  --query QUERY         Input query text
  --domain DOMAIN       Domain to focus on
  --models MODELS       Number of models to use
  --instructions INSTRUCTIONS
                        Number of instructions to use
  --variations VARIATIONS
                        Number of query variations to generate
  --max-combinations MAX_COMBINATIONS
                        Maximum number of combinations to execute
  --output-format {markdown,json}
                        Output format
  --output-file OUTPUT_FILE
                        Path to save the output to
  --simulate            Use simulated responses instead of real model APIs
  --dry-run             Print what would be executed without actually running
```

### Examples

Generate ideas for education innovation using real models:

```bash
python main.py --config sample_config.json --query "How might we redesign education systems to better prepare students for future challenges?" --domain "Education" --models 2 --instructions 5 --variations 3 --max-combinations 15 --output-file "education_ideas.md"
```

Generate ideas for healthcare improvement using simulation mode:

```bash
python main.py --query "How can we make healthcare more accessible and affordable for everyone?" --domain "Healthcare" --models 2 --instructions 3 --variations 2 --output-format json --output-file "healthcare_ideas.json" --simulate
```

Preview what combinations would be executed without actually running them:

```bash
python main.py --query "How might we improve urban transportation?" --domain "Urban Planning" --dry-run
```

### Saving and Loading State

You can save the state of the application to continue work later:

```bash
python main.py --query "How might we improve urban transportation?" --save-state "transportation_state.json"
```

Then load it in a subsequent run:

```bash
python main.py --load-state "transportation_state.json" --output-file "transportation_ideas.md"
```

## Core Components

The ISEE framework consists of four main layers:

1. **Input Layer** - Manages the diversity of models, instructions, queries, and domains
2. **Orchestration Layer** - Handles the generation and execution of combinations
3. **Evaluation Layer** - Analyzes and scores the generated results
4. **Extraction Layer** - Synthesizes and refines the most promising ideas

## Development Roadmap

1. ✅ Integrate with real model APIs
2. Implement more sophisticated evaluation algorithms
3. Add clustering and pattern detection for better synthesis
4. Develop a web-based user interface
5. Add collaborative features for team-based innovation
6. Implement feedback loops to improve the quality of generated ideas
7. Add proper database integration for state management
8. Implement parallel execution for better performance

## Implementation Status

The current implementation is a working prototype that demonstrates the conceptual framework. Current features:

- ✅ Real model API integration with Anthropic (Claude) and OpenAI
- ✅ Configuration-based model setup with fallback to simulation
- ✅ Flexible query generation with multiple variation strategies
- ✅ Diverse instruction templates for cognitive approach variation
- ✅ Domain-specific contextualization
- ✅ Basic evaluation using heuristic-based scoring
- ✅ Simple idea synthesis and extraction

Items still in development:

- Evaluation is based on simple heuristics that could be enhanced with more sophisticated analysis
- Idea synthesis could be improved with more advanced NLP techniques
- Pattern recognition and clustering for better synthesis are planned
- A web-based user interface is on the roadmap
- Proper database integration for state management would improve scalability

## Contributors

This project is based on the meta-framework concept developed by Joseph Fajen.

## License

[License information will be added here]
