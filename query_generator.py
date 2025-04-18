"""
Query Generator Module for ISEE Framework

This module provides functionality for generating variations of input queries
to increase the diversity of perspectives in the idea generation process.
"""

import json
import random
from typing import Dict, Any, List, Optional, Tuple, Set
from uuid import uuid4

class Query:
    """Represents a specific user prompt or question."""
    
    def __init__(self, id: str, text: str, variables: Optional[Dict[str, Any]] = None):
        """Initialize a query.
        
        Args:
            id: Unique identifier for the query.
            text: The query text.
            variables: Optional variables that can be used in instruction templates.
        """
        self.id = id
        self.text = text
        self.variables = variables or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to a dictionary representation.
        
        Returns:
            Dictionary representation of the query.
        """
        return {
            "id": self.id,
            "text": self.text,
            "variables": self.variables
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Query':
        """Create a query from a dictionary representation.
        
        Args:
            data: Dictionary representation of the query.
            
        Returns:
            A new Query instance.
        """
        return cls(
            id=data["id"],
            text=data["text"],
            variables=data.get("variables", {})
        )


class QueryGenerator:
    """Generates variations of queries to explore different perspectives."""
    
    def __init__(self):
        """Initialize the query generator."""
        self.base_queries: Dict[str, Query] = {}
        self.variations: Dict[str, List[Query]] = {}
    
    def add_base_query(self, query: Query) -> None:
        """Add a base query that can be used for generating variations.
        
        Args:
            query: The base query.
        """
        self.base_queries[query.id] = query
        if query.id not in self.variations:
            self.variations[query.id] = []
    
    def generate_variations(self, query_id: str, count: int = 3) -> List[Query]:
        """Generate variations of a base query.
        
        Args:
            query_id: ID of the base query.
            count: Number of variations to generate.
            
        Returns:
            List of query variations.
            
        Raises:
            KeyError: If the base query does not exist.
        """
        if query_id not in self.base_queries:
            raise KeyError(f"No base query with ID '{query_id}'")
        
        base_query = self.base_queries[query_id]
        variations = self._create_variations(base_query, count)
        
        # Store and return the variations
        self.variations[query_id].extend(variations)
        return variations
    
    def _create_variations(self, base_query: Query, count: int) -> List[Query]:
        """Create variations of a query using various strategies.
        
        Args:
            base_query: The base query to create variations from.
            count: Number of variations to create.
            
        Returns:
            List of query variations.
        """
        # Strategies for variation generation
        strategies = [
            self._add_constraints,
            self._change_perspective,
            self._add_context,
            self._rephrase_question,
            self._focus_on_specific_aspect,
            self._adopt_alternative_approach
        ]
        
        variations = []
        used_texts: Set[str] = set()
        
        # Generate variations using random strategies
        attempts = 0
        max_attempts = count * 3  # Allow for some failed attempts
        
        while len(variations) < count and attempts < max_attempts:
            strategy = random.choice(strategies)
            variation = strategy(base_query)
            
            # Check for duplicates
            if variation.text not in used_texts:
                used_texts.add(variation.text)
                variations.append(variation)
            
            attempts += 1
        
        return variations
    
    def _add_constraints(self, base_query: Query) -> Query:
        """Strategy: Add constraints to the query.
        
        Args:
            base_query: The base query.
            
        Returns:
            A new query with added constraints.
        """
        constraints = [
            "with limited resources",
            "within a tight budget",
            "in a short timeframe",
            "with minimal technological infrastructure",
            "without requiring specialized expertise",
            "while ensuring accessibility for all users",
            "while minimizing environmental impact",
            "while adhering to strict regulatory requirements",
            "in a way that can be incrementally implemented",
            "without disrupting existing systems"
        ]
        
        constraint = random.choice(constraints)
        text = f"{base_query.text}, {constraint}?"
        
        # Create a new query
        return Query(
            id=f"{base_query.id}_constraint_{str(uuid4())[:8]}",
            text=text,
            variables={**base_query.variables, "constraint": constraint}
        )
    
    def _change_perspective(self, base_query: Query) -> Query:
        """Strategy: Change the perspective of the query.
        
        Args:
            base_query: The base query.
            
        Returns:
            A new query with a different perspective.
        """
        perspectives = [
            "from the perspective of end users",
            "from a sustainability standpoint",
            "from a business efficiency perspective",
            "for developing countries",
            "for rural communities",
            "for elderly populations",
            "for people with disabilities",
            "for young professionals",
            "for educational institutions",
            "for government agencies"
        ]
        
        perspective = random.choice(perspectives)
        text = f"{base_query.text}, considering it {perspective}?"
        
        # Create a new query
        return Query(
            id=f"{base_query.id}_perspective_{str(uuid4())[:8]}",
            text=text,
            variables={**base_query.variables, "perspective": perspective}
        )
    
    def _add_context(self, base_query: Query) -> Query:
        """Strategy: Add context to the query.
        
        Args:
            base_query: The base query.
            
        Returns:
            A new query with added context.
        """
        contexts = [
            "in the context of rapid urbanization",
            "given the rise of remote work",
            "in the era of climate change",
            "with increasing automation",
            "in light of changing demographics",
            "amidst economic uncertainty",
            "in response to public health challenges",
            "with the rise of data-driven decision making",
            "in societies with aging populations",
            "in regions with rapid technological adoption"
        ]
        
        context = random.choice(contexts)
        text = f"{base_query.text}, {context}?"
        
        # Create a new query
        return Query(
            id=f"{base_query.id}_context_{str(uuid4())[:8]}",
            text=text,
            variables={**base_query.variables, "context": context}
        )
    
    def _rephrase_question(self, base_query: Query) -> Query:
        """Strategy: Rephrase the question with similar meaning.
        
        Args:
            base_query: The base query.
            
        Returns:
            A new query with rephrased question.
        """
        # Extract the core subject from the query (very simplified approach)
        text = base_query.text.lower()
        
        # Simple patterns for rephrasing
        if text.startswith("how might we"):
            rephrased = text.replace("how might we", "what are effective ways to")
        elif text.startswith("what are"):
            rephrased = text.replace("what are", "how might we identify")
        elif text.startswith("how can"):
            rephrased = text.replace("how can", "what strategies would allow us to")
        elif text.startswith("what strategies"):
            rephrased = text.replace("what strategies", "how might we develop approaches to")
        else:
            # If no pattern matches, create a more generic rephrasing
            rephrased = f"What innovative approaches could address the challenge of {text}?"
        
        # Ensure it ends with a question mark
        if not rephrased.endswith("?"):
            rephrased += "?"
        
        # Capitalize the first letter
        rephrased = rephrased[0].upper() + rephrased[1:]
        
        # Create a new query
        return Query(
            id=f"{base_query.id}_rephrased_{str(uuid4())[:8]}",
            text=rephrased,
            variables=base_query.variables.copy()
        )
    
    def _focus_on_specific_aspect(self, base_query: Query) -> Query:
        """Strategy: Focus the query on a specific aspect of the problem.
        
        Args:
            base_query: The base query.
            
        Returns:
            A new query focused on a specific aspect.
        """
        aspects = [
            "the technological aspects of",
            "the social implications of",
            "the economic viability of",
            "the implementation challenges in",
            "the user adoption factors for",
            "the long-term sustainability of",
            "the scalability considerations for",
            "the ethical dimensions of",
            "the educational requirements for",
            "the policy implications of"
        ]
        
        aspect = random.choice(aspects)
        
        # Extract the core concept from the query
        text = base_query.text
        if text.endswith("?"):
            text = text[:-1]
        
        new_text = f"How might we address {aspect} {text}?"
        
        # Create a new query
        return Query(
            id=f"{base_query.id}_aspect_{str(uuid4())[:8]}",
            text=new_text,
            variables={**base_query.variables, "focused_aspect": aspect}
        )
    
    def _adopt_alternative_approach(self, base_query: Query) -> Query:
        """Strategy: Reframe the query to adopt an alternative approach.
        
        Args:
            base_query: The base query.
            
        Returns:
            A new query with an alternative approach.
        """
        approaches = [
            "Instead of conventional solutions, how might we",
            "What if we considered a bottom-up approach to",
            "How could emerging technologies enable us to",
            "What would a nature-inspired solution look like for",
            "How might we leverage collective intelligence to",
            "What cross-industry insights could be applied to",
            "How could behavioral science principles help us",
            "What would a minimalist approach look like for",
            "How might we use gamification to address",
            "What if we focused on prevention rather than solution for"
        ]
        
        approach = random.choice(approaches)
        
        # Extract the core concept from the query
        text = base_query.text.lower()
        if text.startswith("how might we "):
            core = text[13:]
        elif text.startswith("how can "):
            core = text[8:]
        elif text.startswith("what are "):
            core = text[9:]
        else:
            # If no pattern matches, use the whole text
            core = text
        
        if core.endswith("?"):
            core = core[:-1]
        
        new_text = f"{approach} {core}?"
        
        # Create a new query
        return Query(
            id=f"{base_query.id}_approach_{str(uuid4())[:8]}",
            text=new_text,
            variables={**base_query.variables, "alternative_approach": approach}
        )
    
    def load_from_file(self, file_path: str) -> None:
        """Load queries from a JSON file.
        
        Args:
            file_path: Path to the JSON file containing queries.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
            KeyError: If the file does not contain a 'queries' key.
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        queries_data = data.get('queries')
        if not queries_data:
            raise KeyError("File does not contain 'queries' key")
        
        for query_data in queries_data:
            query = Query.from_dict(query_data)
            self.add_base_query(query)
    
    def save_to_file(self, file_path: str) -> None:
        """Save queries and their variations to a JSON file.
        
        Args:
            file_path: Path to save the queries to.
        """
        # Prepare data for serialization
        base_queries = [query.to_dict() for query in self.base_queries.values()]
        all_variations = []
        for variations in self.variations.values():
            all_variations.extend([var.to_dict() for var in variations])
        
        data = {
            'base_queries': base_queries,
            'variations': all_variations
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_all_queries(self) -> List[Query]:
        """Get all queries (both base queries and variations).
        
        Returns:
            List of all queries.
        """
        all_queries = list(self.base_queries.values())
        for variations in self.variations.values():
            all_queries.extend(variations)
        return all_queries
        
    def list_base_queries(self) -> List[Query]:
        """Get only the base queries (not variations).
        
        Returns:
            List of base queries.
        """
        return list(self.base_queries.values())
    
    def get_query_by_id(self, query_id: str) -> Optional[Query]:
        """Get a query by its ID.
        
        Args:
            query_id: ID of the query to get.
            
        Returns:
            The query if found, None otherwise.
        """
        if query_id in self.base_queries:
            return self.base_queries[query_id]
        
        for variations in self.variations.values():
            for query in variations:
                if query.id == query_id:
                    return query
        
        return None


def create_default_queries() -> List[Query]:
    """Create a set of default base queries.
    
    Returns:
        List of default queries.
    """
    defaults = [
        Query(
            id="q_urban_transport",
            text="How might we improve urban transportation in the next decade?",
            variables={"domain": "urban transportation", "timeframe": "next decade"}
        ),
        Query(
            id="q_education",
            text="How might we redesign education systems to better prepare students for future challenges?",
            variables={"domain": "education", "focus": "future preparation"}
        ),
        Query(
            id="q_healthcare",
            text="How might we make healthcare more accessible and affordable for everyone?",
            variables={"domain": "healthcare", "focus": "accessibility and affordability"}
        ),
        Query(
            id="q_climate",
            text="How might we accelerate the transition to sustainable energy sources?",
            variables={"domain": "energy", "focus": "sustainability transition"}
        ),
        Query(
            id="q_food",
            text="How might we transform food systems to be more sustainable and equitable?",
            variables={"domain": "food systems", "focus": "sustainability and equity"}
        )
    ]
    
    return defaults


# Example usage
if __name__ == "__main__":
    # Create a query generator
    generator = QueryGenerator()
    
    # Add default queries
    for query in create_default_queries():
        generator.add_base_query(query)
    
    # Generate variations for the urban transportation query
    urban_variations = generator.generate_variations("q_urban_transport", count=5)
    
    # Print the original query and its variations
    base_query = generator.base_queries["q_urban_transport"]
    print(f"Base Query: {base_query.text}")
    print("\nVariations:")
    for i, var in enumerate(urban_variations, 1):
        print(f"{i}. {var.text}")
        print(f"   ID: {var.id}")
        print(f"   Variables: {var.variables}")
        print()
    
    # Generate variations for the education query
    education_variations = generator.generate_variations("q_education", count=3)
    
    # Print the original query and its variations
    base_query = generator.base_queries["q_education"]
    print(f"\nBase Query: {base_query.text}")
    print("\nVariations:")
    for i, var in enumerate(education_variations, 1):
        print(f"{i}. {var.text}")
        print()
    
    # Save to a file
    import os
    os.makedirs("data", exist_ok=True)
    generator.save_to_file("data/query_variations.json")
    print("\nQueries saved to data/query_variations.json")
