#!/usr/bin/env node

/**
 * Mermaid to Excalidraw Converter
 * 
 * Converts Mermaid diagram text files (.mmd) to Excalidraw format (.excalidraw)
 * 
 * Usage:
 *   node scripts/mermaid-to-excalidraw.js <input.mmd> [output.excalidraw]
 *   node scripts/mermaid-to-excalidraw.js <mermaid-text-string>
 * 
 * Examples:
 *   node scripts/mermaid-to-excalidraw.js diagrams/flow.mmd diagrams/flow.excalidraw
 *   node scripts/mermaid-to-excalidraw.js "graph TD; A-->B; B-->C"
 */

const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

// Set up DOM environment for Node.js
const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>');
global.window = dom.window;
global.document = dom.window.document;
global.navigator = dom.window.navigator;
global.DOMParser = dom.window.DOMParser;
global.XMLSerializer = dom.window.XMLSerializer;

// Now import the mermaid parser
const { parseMermaidToExcalidraw } = require('@excalidraw/mermaid-to-excalidraw');

async function convertMermaidToExcalidraw(mermaidText, outputPath = null) {
  try {
    console.log('Converting Mermaid diagram to Excalidraw...\n');
    
    // Parse the Mermaid diagram
    const { elements, files } = await parseMermaidToExcalidraw(mermaidText, {
      fontSize: 16,
    });

    // Create the Excalidraw file structure
    const excalidrawData = {
      type: 'excalidraw',
      version: 2,
      source: 'https://excalidraw.com',
      elements: elements,
      appState: {
        viewBackgroundColor: '#ffffff',
        gridSize: 20,
      },
      files: files || {},
    };

    // Convert to JSON string
    const jsonOutput = JSON.stringify(excalidrawData, null, 2);

    if (outputPath) {
      // Write to file
      fs.writeFileSync(outputPath, jsonOutput, 'utf8');
      console.log(`✅ Successfully converted to: ${outputPath}`);
      console.log(`📊 Generated ${elements.length} Excalidraw elements`);
    } else {
      // Print to console
      console.log(jsonOutput);
    }

    return excalidrawData;
  } catch (error) {
    console.error('❌ Error converting Mermaid to Excalidraw:');
    console.error(error.message);
    if (error.stack) {
      console.error('\nStack trace:');
      console.error(error.stack);
    }
    process.exit(1);
  }
}

async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log('Usage:');
    console.log('  node scripts/mermaid-to-excalidraw.js <input.mmd> [output.excalidraw]');
    console.log('  node scripts/mermaid-to-excalidraw.js "<mermaid-text-string>"');
    console.log('\nExamples:');
    console.log('  node scripts/mermaid-to-excalidraw.js diagrams/flow.mmd');
    console.log('  node scripts/mermaid-to-excalidraw.js diagrams/flow.mmd output/flow.excalidraw');
    console.log('  node scripts/mermaid-to-excalidraw.js "graph TD; A-->B; B-->C"');
    process.exit(1);
  }

  const input = args[0];
  let mermaidText;
  let outputPath = args[1] || null;

  // Check if input is a file path
  if (fs.existsSync(input)) {
    console.log(`📖 Reading Mermaid file: ${input}`);
    mermaidText = fs.readFileSync(input, 'utf8');
    
    // Auto-generate output path if not provided
    if (!outputPath) {
      const parsedPath = path.parse(input);
      outputPath = path.join(parsedPath.dir, `${parsedPath.name}.excalidraw`);
    }
  } else {
    // Treat input as raw Mermaid text
    console.log('📝 Using provided Mermaid text');
    mermaidText = input;
    
    // If output path not specified, print to console
    if (!outputPath) {
      console.log('ℹ️  No output file specified, will print to console\n');
    }
  }

  await convertMermaidToExcalidraw(mermaidText, outputPath);
}

// Run if called directly
if (require.main === module) {
  main().catch((error) => {
    console.error('Fatal error:', error);
    process.exit(1);
  });
}

module.exports = { convertMermaidToExcalidraw };
