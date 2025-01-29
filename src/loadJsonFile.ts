#!/usr/bin/env ts-node
import * as fs from 'fs';
import * as path from 'path';
import { USDM } from '../datastructure-typescript-models/models/USDM'; // Assuming USDM.ts is in the same directory
import { inspect } from 'util'; // For deep inspection



// Function to load a JSON file and print its content
function loadAndPrintJson(filePath: string): void {
  try {
    // Resolve the absolute path of the file
    const absolutePath = path.resolve(filePath);

    // Read the file contents
    const rawData = fs.readFileSync(absolutePath, 'utf8');

    // Parse the JSON file
    const jsonData = JSON.parse(rawData);

    // Deserialize JSON into the USDM model
    const usdmInstance: USDM = Object.assign(new USDM(), jsonData);

    // Print the USDM instance deeply using `util.inspect`
    console.log('Loaded USDM Instance (Deep Inspection):');
    console.log(inspect(usdmInstance, { depth: null, colors: true })); // Allow unlimited depth with colors for better readability

  } catch (err) {
    console.error('Error loading or parsing JSON file:', err.message);
  }

}

// Example usage: specify the path to the JSON file
const jsonFilePath = '../CDISC_Pilot_Study.json'; // Replace with the actual file path
loadAndPrintJson(jsonFilePath);