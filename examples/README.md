# Pipeworks Conditional Axis - Usage Examples

This directory contains **comprehensive, runnable examples** demonstrating all features of the Pipeworks Conditional Axis library. Each example is fully tested, includes detailed docstrings, and follows Python best practices.

## Running Examples

All examples can be run directly from the command line:

```bash
# From project root
python examples/basic_usage.py
python examples/advanced_usage.py
python examples/integration_example.py
python examples/batch_generation.py
python examples/custom_axes.py
python examples/image_prompt_generation.py

# Or from examples directory
cd examples
python basic_usage.py
```

## Example Files

### Core Examples

#### 1. `basic_usage.py` - Foundation

**Purpose**: Learn the fundamental concepts and basic usage patterns.

**What You'll Learn**:
- Simple generation without seeds (random)
- Reproducible generation with seeds
- Serialization to prompt strings
- Understanding axis structure
- Generating multiple distinct entities

**Best For**: First-time users, getting started tutorials

**Examples Included** (5):
1. Simple generation (random)
2. Reproducible generation (with seeds)
3. Serialization to prompts
4. Understanding axes
5. Multiple distinct entities

```bash
python examples/basic_usage.py
```

#### 2. `advanced_usage.py` - Deep Dive

**Purpose**: Understand the internal mechanics and statistical properties.

**What You'll Learn**:
- How weighted probability distributions work
- Exclusion rules preventing illogical combinations
- Mandatory vs optional axes (AXIS_POLICY)
- Analyzing generation patterns with statistics
- Inspecting raw data structures (CONDITION_AXES, WEIGHTS, EXCLUSIONS)

**Best For**: Power users, understanding the system deeply

**Examples Included** (5):
1. Understanding weighted distributions (with visualization)
2. Exclusion rules in action
3. Mandatory vs optional axes
4. Analyzing generation patterns (500-sample statistical analysis)
5. Inspecting raw data structures

```bash
python examples/advanced_usage.py
```

#### 3. `integration_example.py` - Complete Entities

**Purpose**: Combine all three axis systems for complete character generation.

**What You'll Learn**:
- Combining character, facial, and occupation systems
- Generating multiple complete entities
- Narrative vs visual formatting
- Identifying coherence patterns
- Entity archetype generation (filtering by criteria)

**Best For**: Real-world usage, complete character generation

**Examples Included** (5):
1. Complete entity generation
2. Multiple complete entities (population generation)
3. Narrative vs visual formatting
4. Identifying coherence patterns
5. Entity archetype generation (The Desperate Outlaw, The Respected Merchant, etc.)

```bash
python examples/integration_example.py
```

### Advanced Examples

#### 4. `batch_generation.py` - Scale & Performance

**Purpose**: Efficiently generate large numbers of entities.

**What You'll Learn**:
- Simple batch generation (moderate scale, < 10k)
- Export to JSON format (API responses, configuration)
- Export to CSV format (spreadsheets, databases)
- Filtering and selection from batches
- Memory-efficient streaming (large scale, 100k+)
- Parallel generation patterns (conceptual)

**Best For**: Bulk content generation, data export, performance optimization

**Examples Included** (6):
1. Simple batch generation (20 entities)
2. Export to JSON
3. Export to CSV
4. Filtering and selection (100 entities, filtered by criteria)
5. Memory-efficient streaming (1000 entities without storing all)
6. Parallel generation pattern (conceptual guide)

```bash
python examples/batch_generation.py
```

#### 5. `custom_axes.py` - Extensibility

**Purpose**: Create your own custom axis systems for different domains.

**What You'll Learn**:
- The complete pattern for creating custom axes
- Using shared utilities from `_base.py`
- Defining AXES, POLICY, WEIGHTS, EXCLUSIONS
- Writing generation and serialization functions
- Testing exclusion rules
- Combining custom axes with core systems

**Best For**: Extending the library, domain-specific applications

**Included Systems**:
- **Fantasy Magic System**: affinity, proficiency, manifestation, cost
- **Sci-Fi Technology System**: augmentation, tech_access, integration, stability

**Examples Included** (5):
1. Using custom magic system
2. Using custom tech system
3. Combining custom axes with core systems (fantasy + character, sci-fi + character)
4. Testing exclusion rules
5. Custom axis pattern summary (complete guide)

```bash
python examples/custom_axes.py
```

#### 6. `image_prompt_generation.py` - AI Image Integration

**Purpose**: Generate optimized prompts for AI image generation tools.

**What You'll Learn**:
- Converting conditions to image prompts
- Adding style modifiers (portrait, oil painting, 3D render, etc.)
- Quality-enhanced prompts (photorealistic, artistic, fantasy presets)
- Positive and negative prompts (Stable Diffusion)
- Batch prompt generation for character sets
- Context-specific additions (tavern, market, alley, throne room)
- Prompt engineering best practices

**Best For**: AI image generation, Stable Diffusion/DALL-E/Midjourney integration

**Examples Included** (7):
1. Basic image prompt generation
2. Styled prompts (6 different styles)
3. Quality-enhanced prompts (3 preset types)
4. Positive and negative prompts
5. Batch prompt generation (4-character party)
6. Context-specific additions (4 different scenes)
7. Prompt engineering tips (comprehensive guide)

**Supported Tools**:
- Stable Diffusion (Web UI, ComfyUI)
- DALL-E 3
- Midjourney
- Any text-to-image model

```bash
python examples/image_prompt_generation.py
```

## Example Features

All examples include:

- ✅ **Comprehensive type hints** - Full typing for all functions
- ✅ **Google-style docstrings** - Detailed documentation for every function
- ✅ **Working, executable code** - All examples have `main()` functions and can be run directly
- ✅ **Educational comments** - Explanations of concepts throughout
- ✅ **Multiple demonstrations** - 5-7 examples per file
- ✅ **Full test coverage** - 39 tests in `tests/test_examples.py` (all passing)

## Quick Reference Matrix

| Example | Difficulty | Lines | Examples | Best For |
|---------|-----------|-------|----------|----------|
| `basic_usage.py` | Beginner | 204 | 5 | Getting started |
| `advanced_usage.py` | Intermediate | 267 | 5 | Understanding internals |
| `integration_example.py` | Intermediate | 360 | 5 | Complete characters |
| `batch_generation.py` | Advanced | 441 | 6 | Bulk generation |
| `custom_axes.py` | Advanced | 466 | 5 | Extending library |
| `image_prompt_generation.py` | Advanced | 441 | 7 | AI image generation |

## Learning Path

### For New Users
1. Start with `basic_usage.py` - Learn the fundamentals
2. Try `integration_example.py` - See complete character generation
3. Explore `image_prompt_generation.py` - Practical application

### For Advanced Users
1. `advanced_usage.py` - Understand the internals
2. `batch_generation.py` - Learn performance patterns
3. `custom_axes.py` - Extend the system

### For Specific Use Cases

**AI Image Generation**:
- `basic_usage.py` (sections 1-3)
- `integration_example.py` (section 3)
- `image_prompt_generation.py` (all sections)

**Game Development / MUDs**:
- `basic_usage.py` (all)
- `integration_example.py` (all)
- `batch_generation.py` (sections 1-5)

**Custom Domains (Fantasy, Sci-Fi, Horror)**:
- `advanced_usage.py` (section 5)
- `custom_axes.py` (all)

**Bulk Content Generation**:
- `batch_generation.py` (all)
- `integration_example.py` (section 5)

## Testing

All examples are comprehensively tested in `tests/test_examples.py`:

```bash
# Run example tests
pytest tests/test_examples.py -v

# Run all tests including examples
pytest -v
```

**Test Coverage**:
- 39 tests covering all example functionality
- Import tests (all modules can be imported)
- Function tests (all utility functions work correctly)
- Reproducibility tests (seeds produce consistent results)
- Integration tests (systems work together)
- Edge cases (zero counts, empty inputs, etc.)

## Code Quality

All examples follow strict quality standards:

```bash
# Format check
black examples/ --check --line-length=100

# Lint check
ruff check examples/ --line-length=100

# Type check
mypy examples/ --python-version=3.12 --ignore-missing-imports
```

## Next Steps

After exploring the examples:

1. **Review the API documentation** - See `docs/api/` for detailed function reference
2. **Read the design philosophy** - See `docs/design/00_goblin_laws.md`
3. **Check technical specifications** - See `docs/specifications/`
4. **Try the library in your project** - Install with `pip install -e .`

## Contributing

Found a bug or want to add an example? See:
- Main documentation: `docs/README.md`
- Development guide: `CLAUDE.md`
- API reference: `docs/api/`

## License

GPL-3.0 - See LICENSE file for details.

---

**Questions?** Check the main documentation at `docs/` or visit the GitHub repository.
