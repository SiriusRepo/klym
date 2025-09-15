// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import { LanguageClient, TransportKind } from 'vscode-languageclient/node';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	const serverModule = context.asAbsolutePath('server.js');
	const serverOptions = {
		run: { module: serverModule, transport: TransportKind.ipc },
		debug: { module: serverModule, transport: TransportKind.ipc }
	};

	const clientOptions = {
		documentSelector: [{ scheme: 'file', language: 'klym' }]
	};

	const client = new LanguageClient('klymLanguageServer', 'Klym Language Server', serverOptions, clientOptions);
	client.start();

}

// This method is called when your extension is deactivated
export function deactivate() {}
