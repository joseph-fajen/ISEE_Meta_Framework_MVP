# ISEE Framework Quick Start Guide

This guide provides a quick overview of how to get started with the Idea Synthesis and Extraction Engine prototype.

## Setup

1. **Environment setup**
   ```bash
   # Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **API Keys** (for future integration)
   
   While the current prototype simulates API calls, you'll eventually need API keys:
   ```bash
   # Set environment variables for API keys
   export ANTHROPIC_API_KEY="your-anthropic-api-key"
   export OPENAI_API_KEY="your-openai-api-key"
   ```

## Running Your First Idea Generation Session

Try a simple run to see the framework in action:

```bash
python main.py --query "How might we improve remote work collaboration?" --max-combinations 6
```

This will:
- Create a base query
- Generate variations of the query
- Create combinations with different models, instructions, and domains
- Simulate execution of these combinations
- Evaluate the results
- Synthesize ideas from the top results
- Display the output

## Exploring Different Domains

To focus on a specific domain:

```bash
python main.py --query "How might we design more sustainable packaging?" --domain "Sustainability" --max-combinations 8
```

## Saving Results

Save the output to a file:

```bash
python main.py --query "How can we make cities more livable?" --output-file "livable_cities_ideas.md"
```

## Increasing Diversity

To increase the diversity of generated ideas:

```bash
python main.py --query "How might we reimagine public education?" --models 3 --instructions 5 --variations 4 --max-combinations 15
```

## Saving and Loading State

You can save the current state of your session and resume later:

```bash
# Run a session and save the state
python main.py --query "How might we reduce food waste?" --save-state "food_waste_state.json"

# Later, load the state and continue working
python main.py --load-state "food_waste_state.json" --output-file "food_waste_ideas.md"
```

## Customizing Output Format

Choose between markdown and JSON output formats:

```bash
# Get output in JSON format
python main.py --query "How can we improve healthcare access?" --output-format json

# Get output in Markdown format (default)
python main.py --query "How can we improve healthcare access?" --output-format markdown
```

## Extending the Framework

The modular design allows for easy extension:

1. **Add new instruction templates**
   - Edit `instruction_templates.py` to add new cognitive frameworks

2. **Add new domains**
   - Edit `domain_manager.py` to add new application domains

3. **Implement real API integration**
   - Update `model_api_integration.py` with your API keys and endpoints

4. **Enhance evaluation criteria**
   - Modify `evaluation_scoring.py` to add more sophisticated scoring methods

## Directory Structure

Create the following directories for data storage:

```bash
mkdir -p data/results data/state data/output
```

## Example Workflow

Here's a complete workflow example:

```bash
# 1. Run a query with multiple variations
python main.py --query "How might we reduce carbon emissions in urban areas?" --variations 5 --max-combinations 12 --save-state "data/state/carbon_emissions.json"

# 2. Examine the results
cat data/output/carbon_emissions.md

# 3. Run another related query
python main.py --query "How can we increase adoption of renewable energy?" --domain "Sustainability" --load-state "data/state/carbon_emissions.json" --save-state "data/state/energy_transition.json"

# 4. Combine insights for a comprehensive approach
python main.py --load-state "data/state/energy_transition.json" --output-file "data/output/sustainability_roadmap.md"
```

## Troubleshooting

- **Module not found errors**: Ensure you've activated your virtual environment and installed all requirements
- **API errors**: Check your API keys and connection if using real API integration
- **Memory issues**: Reduce the number of combinations with `--max-combinations` for large runs
- **Data persistence**: Use `--save-state` frequently to avoid losing work

## Next Steps

Once you're comfortable with the basic operation:

1. Try different domains and queries to explore the framework's versatility
2. Experiment with different instruction combinations to find what works best for your use cases
3. Implement real API integration for more powerful idea generation
4. Add custom evaluation criteria specific to your domain
5. Develop your own synthesis methods to extract the most value from the generated ideas
