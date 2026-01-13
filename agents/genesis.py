import os
import sys
import argparse
import subprocess
import pathlib
import shutil

class GenesisAgent:
    def __init__(self, target_path, vault_path, intent, heal=False):
        self.target_path = pathlib.Path(target_path).absolute()
        self.vault_path = pathlib.Path(vault_path).absolute()
        self.intent = intent
        self.heal_mode = heal
        self.engine_source = pathlib.Path(__file__).parent.absolute()
        
        mode_str = "⚕️ Modo CURA (Healing)" if self.heal_mode else "🚀 Modo GÊNESE (Genesis)"
        print(f"🧬 Antigravity Agent: {mode_str}")
        print(f"📍 Destino: {self.target_path}")
        print(f"🎯 Intenção: {self.intent}")

    def run(self):
        # 1. Garantir diretório de destino
        self.target_path.mkdir(parents=True, exist_ok=True)
        
        if self.heal_mode:
            self._heal_workspace()
        else:
            # 2. Configurar Links do Obsidian (Zero Copy)
            self._setup_obsidian_links()
            # 3. Enxertar o Motor (Grafting)
            self._graft_engine()
            # 4. Inicializar Workspace (Git, Rules)
            self._initialize_workspace()
        
        print(f"\n✨ Operação concluída com sucesso em {self.target_path}")
        print(f"Execute 'python benchmark_trio.py' no destino para validar.")

    def _heal_workspace(self):
        print("\n🔍 Auditando workspace existente...")
        components = {
            ".agent": "Estrutura de DNA",
            "agents": "Cérebro/Arquiteto",
            "DomiKnowS_Source": "Biblioteca de Lógica"
        }
        
        missing = []
        for path_name, desc in components.items():
            path = self.target_path / path_name
            if not path.exists():
                print(f"❌ Ausente: {desc} ({path_name})")
                missing.append(path_name)
            else:
                print(f"✅ Presente: {desc}")

        if not missing:
            print("\n✔️ Workspace parece robusto. Re-sincronizando DNA...")
        else:
            print(f"\n🛠️ Reparando componentes ausentes: {missing}")

        # Independente de estar ausente, re-sincronizamos os links e enxertamos o motor
        self._setup_obsidian_links()
        self._graft_engine()
        
        # Se não houver arquivo de regras, inicializamos um
        rules_file = self.target_path / "domiknows_rules.py"
        if not rules_file.exists():
            self._initialize_workspace()

    def _setup_obsidian_links(self):
        print("\n🔗 Conectando DNA do Obsidian...")
        agent_dir = self.target_path / ".agent"
        rules_dir = agent_dir / "rules"
        workflows_dir = agent_dir / "workflows"
        
        for d in [agent_dir, rules_dir, workflows_dir]:
            d.mkdir(exist_ok=True)
            
        templates_path = self.vault_path / "10_Rascunhos" / "_Templates"
        
        links = {
            "00_MASTER_Guardrails.md": "02_Guardrails.md",
            "00_MASTER_Seguranca.md": "05_Seguranca-e-Segredos.md",
            "01_PROJECT_Context.md": "01_Base-de-Conhecimento.md"
        }
        
        for link_name, target_name in links.items():
            dest = rules_dir / link_name if "Guardrails" in link_name or "Seguranca" in link_name else agent_dir / link_name
            src = templates_path / target_name
            
            if src.exists():
                self._create_symlink(dest, src)
            else:
                print(f"⚠️ Template não encontrado: {src}")

    def _graft_engine(self):
        print("\n💉 Enxertando Motor (Grafting)...")
        # Pastas a serem copiadas/linkadas do engine_source
        core_folders = ["agents", "DomiKnowS_Source"]
        files_to_copy = ["benchmark_trio.py", "flavius.py"] # Template de teste e Executivo
        
        for folder in core_folders:
            src = self.engine_source / folder
            dest = self.target_path / folder
            if src.exists():
                # No Linux/Codespaces usamos Symlink. No Windows, se possível, também.
                self._create_symlink(dest, src)
            else:
                print(f"⚠️ Motor Core não encontrado: {src}")
                
        for f in files_to_copy:
            src = self.engine_source / f
            dest = self.target_path / f
            if src.exists() and not dest.exists():
                shutil.copy2(src, dest)
                print(f"[OK] Arquivo copiado: {f}")

    def _initialize_workspace(self):
        print("\n🛠️ Inicializando estrutura de regras...")
        
        # Criar domiknows_rules.py básico
        rules_file = self.target_path / "domiknows_rules.py"
        if not rules_file.exists():
            content = f'# Regras Lógicas para: {self.intent}\n'
            content += 'from domiknows.graph import Graph, Concept, Relation\n\n'
            content += 'with Graph("ManifestedGraph") as graph:\n'
            content += '    # Adicione seus conceitos aqui\n'
            content += '    pass\n'
            
            with open(rules_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[OK] Arquivo de regras inicializado: {rules_file.name}")

    def _create_symlink(self, link, target):
        if link.exists():
            if link.is_symlink():
                print(f"ℹ️ Link já existe: {link.name}")
                return
            else:
                print(f"⚠️ Caminho existe e não é link: {link.name}. Pulando.")
                return
                
        try:
            # Em sistemas Windows, pode precisar de privilégios admin para symlink
            # Em Codespaces/Linux é nativo.
            os.symlink(target, link, target_is_directory=target.is_dir())
            print(f"[OK] Link criado: {link.name} -> {target.name}")
        except Exception as e:
            print(f"❌ Falha ao criar link {link.name}: {e}")

# Genesis Logic is now library-only. Invoked by flavius.py
