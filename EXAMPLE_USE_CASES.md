# ISEE Framework Example Use Cases

This document provides three detailed example use cases for the ISEE framework, each showcasing different aspects of the system. Follow these examples to understand the framework's capabilities and how it can be applied to various innovation challenges.

## Use Case 1: Product Innovation - Reimagining Smart Home Interfaces

### Scenario
You're a product designer tasked with developing next-generation interfaces for smart home systems. You want to move beyond screen-based and voice-based interactions to create more intuitive and seamless user experiences.

### Command

```bash
python main.py --config sample_config.json --query "How might we create more intuitive and seamless interfaces for smart home systems beyond screens and voice?" --models 3 --instructions 3 --variations 3 --max-combinations 12 --save-state "data/state/smart_home_interfaces.json" --output-file "data/output/smart_home_interfaces.md"
```

### What This Does

This command:
1. Creates 3 variations of your base query, exploring different perspectives
2. Uses all 3 models from your configuration
3. Applies 3 different cognitive frameworks (analytical, creative, critical, etc.)
4. Generates 12 combinations of these inputs
5. Saves the full state for future reference
6. Outputs the synthesized ideas to a markdown file

### How to Build Upon Results

After reviewing the initial output:

1. **Explore specific aspects**: Focus on promising ideas from the initial run:

```bash
python main.py --load-state "data/state/smart_home_interfaces.json" --query "How might we use ambient environmental cues as interfaces for smart homes?" --max-combinations 5 --save-state "data/state/ambient_interfaces.json"
```

2. **Try different synthesis methods**:

```bash
python main.py --load-state "data/state/smart_home_interfaces.json" --synthesize-method "cross_pollination" --output-file "data/output/cross_pollinated_interfaces.md"
```

## Use Case 2: Addressing Climate Change in Urban Environments

### Scenario
You're working with a city planning department to develop innovative strategies for making urban areas more resilient to climate change while improving quality of life for residents.

### Command

```bash
python main.py --config sample_config.json --query "How might we transform urban environments to address climate change while improving quality of life?" --domain "Urban Planning" --models 2 --instructions 5 --variations 4 --max-combinations 15 --save-state "data/state/climate_resilient_cities.json" --output-file "data/output/climate_resilient_cities.md"
```

### What This Does

This command:
1. Focuses on the "Urban Planning" domain for relevant context
2. Uses 2 different AI models
3. Applies 5 different cognitive frameworks to maximize diversity of thinking
4. Creates 4 variations of the query to explore different angles
5. Generates 15 combinations for a substantial exploration
6. Saves the state and outputs the results to a markdown file

### How to Build Upon Results

After the initial exploration:

1. **Add constraints to make ideas more practical**:

```bash
python main.py --load-state "data/state/climate_resilient_cities.json" --query "How might we transform urban environments to address climate change while improving quality of life, with limited budgets and minimal disruption to existing infrastructure?" --max-combinations 8 --save-state "data/state/practical_climate_solutions.json"
```

2. **Export detailed ideas for further analysis**:

```bash
python main.py --load-state "data/state/climate_resilient_cities.json" --output-format json --output-file "data/output/climate_solutions_detailed.json"
```

## Use Case 3: Reinventing Technical Documentation with AI

### Scenario
You're a technical documentation team lead trying to revolutionize how your company creates, maintains, and delivers documentation using AI technologies.

### Command

```bash
python main.py --config sample_config.json --query "How might we reinvent technical documentation processes and deliverables using AI?" --models 3 --instructions 4 --variations 3 --max-combinations 10 --dry-run
```

First run this with `--dry-run` to preview the combinations. Then run the actual command:

```bash
python main.py --config sample_config.json --query "How might we reinvent technical documentation processes and deliverables using AI?" --models 3 --instructions 4 --variations 3 --max-combinations 10 --save-state "data/state/ai_documentation.json" --output-file "data/output/ai_documentation.md"
```

### What This Does

This command:
1. Uses all 3 models for diverse AI perspectives
2. Applies 4 different cognitive frameworks
3. Creates 3 variations of the query
4. Generates 10 combinations
5. First previews what would run (with dry-run)
6. Then saves the state and results

### How to Build Upon Results

To maximize the value from this exploration:

1. **Evaluate the top results individually**:

```bash
python result_viewer.py --state "data/state/ai_documentation.json" --interactive
```

2. **Create a focused follow-up session**:

```bash
python main.py --query "How might we implement real-time collaborative editing in technical documentation with AI assistance?" --models 2 --instructions 2 --variations 2 --max-combinations 5 --save-state "data/state/collaborative_documentation.json"
```

3. **Combine insights from both sessions**:

```bash
# Export both state files to markdown
python main.py --load-state "data/state/ai_documentation.json" --output-file "data/output/general_ai_doc.md"
python main.py --load-state "data/state/collaborative_documentation.json" --output-file "data/output/collaborative_ai_doc.md"

# Manual review and synthesis of both outputs
```

## Tips for Creating Your Own Use Cases

1. **Start with a clear, open-ended question** that defines your innovation challenge
2. **Adjust parameters based on your needs**:
   - More `--variations` for exploring different perspectives
   - More `--instructions` for diverse cognitive approaches
   - More `--models` for different AI "personalities"
   - Higher `--max-combinations` for broader exploration

3. **Use domain constraints** to focus on specific contexts
4. **Save state files** to build cumulative knowledge
5. **Use the Result Viewer** to dive deeper into specific outputs
6. **Follow promising threads** with targeted follow-up queries
7. **Experiment with different synthesis methods** to extract maximum value

## Advanced Example: Multi-Stage Innovation Process

For complex innovation challenges, consider a multi-stage process:

```bash
# Stage 1: Broad exploration
python main.py --config sample_config.json --query "How might we revolutionize remote work collaboration?" --models 3 --instructions 5 --variations 4 --max-combinations 20 --save-state "data/state/remote_work_stage1.json"

# Stage 2: Focus on promising themes (after reviewing Stage 1 results)
python main.py --query "How might we create immersive virtual collaboration spaces that preserve non-verbal communication?" --load-state "data/state/remote_work_stage1.json" --max-combinations 10 --save-state "data/state/remote_work_stage2.json"

# Stage 3: Add constraints for practical implementation
python main.py --query "How might we create immersive virtual collaboration spaces that work on standard hardware and low-bandwidth connections?" --load-state "data/state/remote_work_stage2.json" --max-combinations 8 --save-state "data/state/remote_work_stage3.json" --output-file "data/output/practical_virtual_collaboration.md"
```

This multi-stage approach demonstrates how ISEE can support an entire innovation process from initial exploration to practical implementation.