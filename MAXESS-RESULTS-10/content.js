/* =========================================================
   MAXESS RESULTS — CONTENT SYSTEM
   The visual layer and assessment engine are separate from
   the language layer. This allows future assessments and
   white-label versions to reuse the same Results experience.
========================================================= */
window.MAXESS_CONTENT = {
  version: 'MAXESS-CONTENT-1',

  levels: {
    Foundation: {
      title: 'You are building the foundation.',
      subtitle: 'The fundamentals create the fastest early gains.',
      explanation: 'You are beginning to discover how much better AI becomes when your own thinking is clear. Your next step is not complexity. It is deliberate direction.',
      action: 'Learn to define the goal, provide the context and judge the result before adding more advanced techniques.'
    },
    Developing: {
      title: 'You are developing real AI fluency.',
      subtitle: 'Your instincts are becoming a usable process.',
      explanation: 'You already have patterns that work. The opportunity is consistency: taking what works sometimes and turning it into something you can repeat on purpose.',
      action: 'Build a simple repeatable workflow around the parts of AI work you do most often.'
    },
    Advancing: {
      title: 'You are operating at an advancing level.',
      subtitle: 'You can direct AI instead of merely requesting from it.',
      explanation: 'Your profile shows that you already understand an important truth: the human side of the interaction determines much of the quality of the result.',
      action: 'Use scorecards, iteration and systems thinking to turn strong individual interactions into compounding capability.'
    },
    Mastering: {
      title: 'You are approaching mastery.',
      subtitle: 'The next gains come from refinement and leverage.',
      explanation: 'Your fundamentals are strong enough that small improvements in judgment, process and system design can create disproportionate returns.',
      action: 'Teach your process, automate repeatable work and continually raise the standards by which you evaluate outputs.'
    }
  },

  dimensions: {
    direction: {
      title: 'Direction',
      question: 'Do you know where you are going before asking AI to move?',
      low: 'When direction is unclear, even a technically impressive answer can solve the wrong problem.',
      middle: 'You usually know the destination, but sometimes leave success conditions implicit.',
      high: 'You establish purpose, priorities and constraints before asking AI to create.',
      master: 'You can translate complex outcomes into clear objectives that guide people and AI together.',
      practice: 'Write the desired outcome in one sentence before opening the prompt box.',
      signal: 'Strong direction reduces wasted output.'
    },
    communication: {
      title: 'Communication',
      question: 'Can AI understand what you mean without having to guess?',
      low: 'Missing context forces AI to fill gaps with assumptions.',
      middle: 'You provide useful context but may leave audience, tone or constraints unstated.',
      high: 'You communicate intent, context, examples and expectations with deliberate clarity.',
      master: 'You can shape communication so precisely that the desired output becomes easier to predict and refine.',
      practice: 'Add audience, purpose, constraints and one example to an important request.',
      signal: 'Clearer human communication creates clearer machine output.'
    },
    evaluation: {
      title: 'Evaluation',
      question: 'Can you tell whether an AI answer is actually good?',
      low: 'Without a standard, confidence can be mistaken for quality.',
      middle: 'You can spot obvious problems but may rely on intuition for subtle quality judgments.',
      high: 'You compare important outputs against explicit criteria before accepting them.',
      master: 'You create strong evaluation systems that make quality visible, measurable and improvable.',
      practice: 'Write three criteria that an important AI answer must satisfy before you accept it.',
      signal: 'You do not need a better answer if you do not know how to recognize a better answer.'
    },
    iteration: {
      title: 'Iteration',
      question: 'Do you improve the first answer or simply accept it?',
      low: 'Stopping at version one leaves much of AI’s potential unused.',
      middle: 'You revise when something is obviously wrong, but the second pass may not be systematic.',
      high: 'You score the draft, identify the largest gap and deliberately request another pass.',
      master: 'You run disciplined improvement loops that compound quality and speed over time.',
      practice: 'For your next important result, ask: “What is the single biggest reason this is not a 10?”',
      signal: 'The first version is a starting point, not a finish line.'
    },
    systemsThinking: {
      title: 'Systems Thinking',
      question: 'Can one successful interaction become a repeatable system?',
      low: 'Useful work may remain trapped inside one-off conversations.',
      middle: 'You recognize useful workflows but may not capture them consistently.',
      high: 'You connect prompts, tools, people and outputs into repeatable processes.',
      master: 'You design systems that preserve learning and compound value across projects.',
      practice: 'After completing a task twice, write down the repeatable sequence that produced it.',
      signal: 'Systems turn individual wins into durable capability.'
    }
  },

  pathways: {
    direction: {
      title: 'Define the destination',
      detail: 'Before asking AI to produce anything important, write what success looks like. Add the audience, purpose and constraints.',
      habit: 'One-sentence outcome before every high-value request.'
    },
    communication: {
      title: 'Make the invisible visible',
      detail: 'Tell AI the context it cannot know: why this matters, who will use it, what tone is required and what must not happen.',
      habit: 'Context before complexity.'
    },
    evaluation: {
      title: 'Build your scorecard',
      detail: 'Choose a handful of criteria before judging an output. This changes AI work from “I think it is good” into a process you can improve.',
      habit: 'Score before accepting.'
    },
    iteration: {
      title: 'Never stop at version one',
      detail: 'Use the first answer to expose what is missing. Then score it, give targeted feedback and run another pass.',
      habit: 'Every important result gets a second pass.'
    },
    systemsThinking: {
      title: 'Turn wins into systems',
      detail: 'When a process works, capture it. Give it a name, steps, inputs, outputs and a standard for success.',
      habit: 'If you do it twice, consider systemizing it.'
    }
  },

  method: {
    KNOW: 'Understand the real goal, context, audience, constraints and current state before you act.',
    TELL: 'Give AI the information, perspective and boundaries it needs to reason in the right direction.',
    ASK: 'Make the request explicit. Ask for the transformation, decision, creation or analysis you actually need.',
    CREATE: 'Let AI produce a first useful version. Do not confuse creation with completion.',
    SCORE: 'Judge the output. Compare it against the standards that matter to the real user and the real goal.',
    IMPROVE: 'Identify the highest-value weakness and give specific feedback that changes the next version.',
    REPEAT: 'Run the loop again. Quality becomes a habit when improvement becomes part of the process.'
  },

  microcopy: {
    scoreLabel: 'YOUR MAXESS SCORE',
    fingerprintLabel: 'YOUR FIVE-DIMENSION FINGERPRINT',
    advantageLabel: 'YOUR NATURAL ADVANTAGE',
    opportunityLabel: 'YOUR HIGHEST-LEVERAGE OPPORTUNITY',
    insightLabel: 'THE PATTERN WE FOUND',
    pathwayLabel: 'YOUR NEXT THREE MOVES',
    methodLabel: 'THE MAXESS OPERATING LOOP',
    nayaLabel: 'YOUR PERSONALIZED NAYA REPORT',
    nextLabel: 'WHAT COMES NEXT'
  },

  whyTemplates: [
    'Your strongest ability is not an accident. It is a behavior you can deliberately reuse.',
    'Your lowest dimension is not a weakness to be ashamed of. It is a map showing where effort can create leverage.',
    'The gap between your current score and your next level is usually a process problem, not a talent problem.',
    'Mastery grows when you stop asking only whether AI can do something and start asking how you can direct, judge and improve it.',
    'The goal is not to become more dependent on AI. The goal is to become more capable with AI.'
  ],

  callsToAction: [
    'Run one deliberate second pass today.',
    'Create a scorecard for your next important AI task.',
    'Turn one repeated AI task into a reusable workflow.',
    'Teach someone else the MAXESS loop.',
    'Return to your Results after you have practiced your opportunity dimension.'
  ]
};
