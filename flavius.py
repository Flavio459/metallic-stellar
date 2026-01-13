#!/usr/bin/env python3
"""
🏛️ MOTOR FLAVIUS (Antigime) v1.0
--------------------------------
O Executivo Central unificado.
Controla o Gênese, a Cura e a Execução Lógica.

Uso:
  python flavius.py genesis --target "./NovoProjeto"
  python flavius.py heal --target "./ProjetoExistente"
  python flavius.py exec "Minha intenção" --dna hvac_rules.yaml
"""

import sys
import os
import argparse
from pathlib import Path

# Add local modules to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Import Agents
try:
    from agents.genesis import GenesisAgent
    from agents.flavius_host import AntigravityHost as FlaviusHost # Renamed alias
except ImportError as e:
    print(f"❌ Erro Crítico: Falha ao importar agentes. {e}")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="🏛️ Motor Flavius: O Imperador da Lógica")
    subparsers = parser.add_subparsers(dest="command", help="Comandos do Império")

    # --- COMANDO: GENESIS (Criar) ---
    cmd_genesis = subparsers.add_parser("genesis", help="Cria um novo workspace")
    cmd_genesis.add_argument("--target", required=True, help="Onde criar o domínio?")
    cmd_genesis.add_argument("--vault", required=True, help="Caminho do Obsidian Vault")
    cmd_genesis.add_argument("--intent", default="New Project", help="Descrição do projeto")

    # --- COMANDO: HEAL (Curar) ---
    cmd_heal = subparsers.add_parser("heal", help="Cura um workspace existente")
    cmd_heal.add_argument("--target", required=True, help="Projeto a ser curado")
    cmd_heal.add_argument("--vault", required=True, help="Caminho do Obsidian Vault")

    # --- COMANDO: EXEC (Executar) ---
    cmd_exec = subparsers.add_parser("exec", help="Executa uma intenção lógica")
    cmd_exec.add_argument("prompt", help="A intenção do usuário (ex: 'Orçamento para sala X')")
    cmd_exec.add_argument("--dna", default=None, help="Arquivo YAML de regras (DNA)")

    args = parser.parse_args()

    print("\n🏛️  FLAVIUS ENGINE ONLINE")
    print("=========================")

    if args.command == "genesis":
        print(f"🚀 Iniciando Gênese em: {args.target}")
        agent = GenesisAgent(args.target, args.vault, args.intent, heal=False)
        agent.run()

    elif args.command == "heal":
        print(f"⚕️  Iniciando Protocolo de Cura em: {args.target}")
        agent = GenesisAgent(args.target, args.vault, intent="Healing", heal=True)
        agent.run()

    elif args.command == "exec":
        print(f"⚡ Executando Lógica: '{args.prompt}'")
        dna_path = args.dna
        
        # Auto-detect DNA if not provided and inside a valid workspace
        if not dna_path and os.path.exists("hvac_rules.yaml"):
            dna_path = "hvac_rules.yaml"
            print(f"🧬 DNA detectado automaticamente: {dna_path}")
            
        host = FlaviusHost(domain_yaml=dna_path)
        host.process_user_intent(args.prompt)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
