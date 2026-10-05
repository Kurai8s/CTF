# game.py (Versi Final: Level 1 - 10)

class TerminalGame:
    def __init__(self):
        self.active_procs = {}
        self.env_vars = {}
        self.load_level(1)

    def load_level(self, lvl):
        self.level = lvl
        self.cwd = []
        if lvl == 1:
            self.fs = {"home": {"guest": {"briefing.txt": "Cari password di /var/log/auth.log"}}, "var": {"log": {"auth.log": "Failed...\nSUCCESS: pass=SHADOW_NET"}}}
            self.cwd = ["home", "guest"]
            print("\n=== LEVEL 1: RECONNAISSANCE ===\nMisi: Temukan password. Submit dengan: submit [password]")
        elif lvl == 2:
            self.fs = {"root": {"exploit.sh": {"content": "echo 'KEY: ESCALATION_99'", "perms": "-"}}}
            self.cwd = ["root"]
            print("\n=== LEVEL 2: PRIVILEGE ESCALATION ===\nMisi: File terkunci. Ubah izin, eksekusi, dan submit KEY-nya.")
        elif lvl == 3:
            self.fs = {"intel": {"data.txt": "Rahasia negara"}, "tmp": {}, "drop": {}}
            self.cwd = ["intel"]
            print("\n=== LEVEL 3: EXFILTRATION ===\nMisi: Kompres data.txt (gzip), pindahkan ke /drop/ (mv). Submit 'DONE' jika selesai.")
        elif lvl == 4:
            self.active_procs = {"101": "systemd", "202": "sshd", "999": "FIREWALL_BLOCK"}
            self.fs = {"home": {"agent": {"briefing.txt": "Matikan proses FIREWALL_BLOCK (PID 999), lalu submit."}}}
            self.cwd = ["home", "agent"]
            print("\n=== LEVEL 4: SYSTEM HIJACK ===\nMisi: Gunakan 'ps' untuk lihat proses, 'kill [PID]' untuk mematikan.")
        elif lvl == 5:
            self.fs = {"home": {"agent": {"briefing.txt": "Ambil token dari API lokal."}}}
            self.cwd = ["home", "agent"]
            print("\n=== LEVEL 5: NETWORK RECON ===\nMisi: Gunakan 'curl' untuk mengambil token dari http://localhost/api/token. Submit token tersebut.")
        elif lvl == 6:
            self.fs = {"var": {"www": {"html": {"backup": {"old_2020": {"hidden_key.txt": "FORENSIC_MASTER"}}}}}}
            self.cwd = ["var", "www"]
            print("\n=== LEVEL 6: FORENSICS ===\nMisi: File 'hidden_key.txt' hilang. Gunakan 'find [dir] -name [file]' untuk menemukannya. Submit isinya.")
        elif lvl == 7:
            self.fs = {"var": {"log": {"syslog": "INFO: boot\nERROR: disk fail\nINFO: run\nERROR: net fail\nERROR: mem fail\nINFO: done"}}}
            self.cwd = ["var", "log"]
            print("\n=== LEVEL 7: LOG ANALYSIS ===\nMisi: Hitung berapa kali 'ERROR' muncul di syslog. Gunakan 'grep -c [kata] [file]'. Submit angkanya.")
        elif lvl == 8:
            self.fs = {"home": {"agent": {".secret_config": {"content": "OCTAL_KEY_88", "perms": "-"}}}}
            self.cwd = ["home", "agent"]
            print("\n=== LEVEL 8: HIDDEN & OCTAL ===\nMisi: File tersembunyi (.). Gunakan 'ls -a', ubah izin dengan 'chmod 777', baca, dan submit.")
        elif lvl == 9:
            self.fs = {"home": {"agent": {"payload.tar": {"content": "ARCHIVE_MASTER_99", "type": "tar"}}}}
            self.cwd = ["home", "agent"]
            print("\n=== LEVEL 9: ARCHIVING ===\nMisi: Ekstrak payload.tar menggunakan 'tar -xvf [file]', baca isinya, dan submit.")
        elif lvl == 10:
            self.fs = {"home": {"agent": {"briefing.txt": "Kunci final ada di environment variable."}}}
            self.cwd = ["home", "agent"]
            print("\n=== LEVEL 10: ENVIRONMENT VARIABLES ===\nMisi: Set variabel 'FINAL_KEY=CYBER_GOD_10' dengan 'export', cek dengan 'echo $FINAL_KEY', lalu submit.")

    def get_node(self, path=None):
        node = self.fs
        for p in (path or self.cwd):
            if isinstance(node, dict) and p in node: node = node[p]
            else: return None
        return node

    def get_dest_info(self, dest_path_str, src_name):
        if dest_path_str.endswith("/"):
            path_to_check = dest_path_str.rstrip("/")
            parts = [p for p in path_to_check.split("/") if p]
            target_path = parts if dest_path_str.startswith("/") else self.cwd + parts
            target_node = self.get_node(target_path)
            if isinstance(target_node, dict) and "content" not in target_node:
                return self.get_node(target_path), src_name

        if dest_path_str.startswith("/"):
            parts = [p for p in dest_path_str.split("/") if p]
            target_path = parts
        else:
            parts = [p for p in dest_path_str.split("/") if p]
            target_path = self.cwd + parts

        target_node = self.get_node(target_path)

        if isinstance(target_node, dict) and "content" not in target_node:
            return target_node, src_name
        else:
            if dest_path_str.startswith("/"):
                dir_path_parts = parts[:-1]
                filename = parts[-1] if parts else src_name
            else:
                dir_path_parts = self.cwd + parts[:-1]
                filename = parts[-1] if parts else src_name
            
            dir_node = self.get_node(dir_path_parts) if dir_path_parts else self.fs
            return dir_node, filename

    def run(self):
        while True:
            path_str = "/".join(self.cwd) or "/"
            cmd_parts = input(f"agent@target:~/{path_str}$ ").strip().split()
            if not cmd_parts: continue
            cmd, args = cmd_parts[0], cmd_parts[1:]

            if cmd == "exit": break
            elif cmd == "cd": self.cmd_cd(args)
            elif cmd == "ls": self.cmd_ls(args)
            elif cmd == "cat": self.cmd_cat(args)
            elif cmd == "grep": self.cmd_grep(args)
            elif cmd == "chmod": self.cmd_chmod(args)
            elif cmd.startswith("./"): self.cmd_exec(cmd[2:])
            elif cmd == "cp": self.cmd_cp(args)
            elif cmd == "mv": self.cmd_mv(args)
            elif cmd == "gzip": self.cmd_gzip(args)
            elif cmd == "ps": self.cmd_ps()
            elif cmd == "kill": self.cmd_kill(args)
            elif cmd == "curl": self.cmd_curl(args)
            elif cmd == "find": self.cmd_find(args)
            elif cmd == "tar": self.cmd_tar(args)
            elif cmd == "export": self.cmd_export(args)
            elif cmd == "echo": self.cmd_echo(args)
            elif cmd == "submit": self.cmd_submit(args)
            elif cmd == "restart": self.load_level(self.level)
            elif cmd == "level": 
                if args and args[0].isdigit() and 1 <= int(args[0]) <= 10:
                    self.load_level(int(args[0]))
                else:
                    print("Usage: level [1-10]")
            elif cmd == "help": print("cd, ls [-a], cat, grep [-c], chmod, ./[file], cp, mv, gzip, ps, kill, curl, find, tar, export, echo, submit, level [1-10], restart")
            else: print(f"bash: {cmd}: command not found")

    def cmd_ls(self, args=None):
        show_hidden = args and "-a" in args
        target_path = args[0] if args and args[0] != "-a" else None
        
        if target_path:
            if target_path.startswith("/"):
                path_parts = [p for p in target_path.split("/") if p]
                node = self.get_node(path_parts)
            else:
                node = self.get_node(self.cwd + [target_path])
        else:
            node = self.get_node()
        
        if isinstance(node, dict) and "content" not in node:
            files = [k for k in node.keys() if show_hidden or not k.startswith(".")]
            print("  ".join(files))
        else:
            print(f"ls: cannot access '{target_path or '.'}': Not a directory")

    def cmd_cd(self, args):
        if not args or args[0] == "~": self.cwd = []; return
        if args[0] == "..":
            if self.cwd: self.cwd.pop()
        elif args[0].startswith("/"): 
            self.cwd = [p for p in args[0].split("/") if p]
        else:
            node = self.get_node(self.cwd + [args[0]])
            if isinstance(node, dict) and "content" not in node: self.cwd.append(args[0])
            else: print(f"cd: {args[0]}: Not a directory")

    def cmd_cat(self, args):
        if not args: return
        node = self.get_node(self.cwd + [args[0]])
        if isinstance(node, dict) and "content" in node:
            print(node["content"]) if 'r' in node.get("perms", "r") else print("Permission denied")
        elif isinstance(node, str): print(node)
        else: print(f"cat: {args[0]}: No such file")

    def cmd_grep(self, args):
        if not args: return
        if args[0] == "-c" and len(args) >= 3:
            pattern, filename = args[1], args[2]
            node = self.get_node(self.cwd + [filename])
            if isinstance(node, str) or (isinstance(node, dict) and "content" in node):
                content = node if isinstance(node, str) else node["content"]
                print(sum(1 for line in content.split('\n') if pattern in line))
            else: print(f"grep: {filename}: No such file")
            return
        if len(args) < 2: return
        node = self.get_node(self.cwd + [args[1]])
        if isinstance(node, str):
            for line in node.split('\n'):
                if args[0] in line: print(line)
        elif isinstance(node, dict) and "content" in node:
            for line in node["content"].split('\n'):
                if args[0] in line: print(line)

    def cmd_chmod(self, args):
        if len(args) < 2: return
        node = self.get_node(self.cwd + [args[1]])
        if isinstance(node, dict) and "content" in node:
            if '+x' in args[0] or args[0] == '777': node["perms"] = node.get("perms", "") + 'x' + 'r'
            print(f"Mode changed.")

    def cmd_exec(self, filename):
        node = self.get_node(self.cwd + [filename])
        if isinstance(node, dict) and "content" in node:
            if 'x' in node.get("perms", ""):
                content = node["content"]
                print(content.replace("echo '", "").replace("'", "")) if content.startswith("echo") else print("Executed.")
            else: print(f"bash: ./{filename}: Permission denied")

    def cmd_cp(self, args):
        if len(args) < 2: return
        src_name, dest_path_str = args[0], args[1]
        src_node = self.get_node(self.cwd + [src_name])
        if not (isinstance(src_node, str) or (isinstance(src_node, dict) and "content" in src_node)):
            print(f"cp: cannot stat '{src_name}': No such file or directory"); return
        dir_node, filename = self.get_dest_info(dest_path_str, src_name)
        if isinstance(dir_node, dict): dir_node[filename] = src_node; print(f"Copied to {dest_path_str}")
        else: print(f"cp: target '{dest_path_str}' is not a directory")

    def cmd_mv(self, args):
        if len(args) < 2: return
        src_name, dest_path_str = args[0], args[1]
        src_dir = self.get_node()
        if src_name not in src_dir: print(f"mv: cannot stat '{src_name}': No such file or directory"); return
        dir_node, filename = self.get_dest_info(dest_path_str, src_name)
        if isinstance(dir_node, dict): dir_node[filename] = src_dir[src_name]; del src_dir[src_name]; print(f"Moved to {dest_path_str}")
        else: print(f"mv: target '{dest_path_str}' is not a directory")

    def cmd_gzip(self, args):
        if not args: return
        src_dir = self.get_node()
        if args[0] in src_dir and isinstance(src_dir[args[0]], str):
            src_dir[args[0] + ".gz"] = "compressed_data"; del src_dir[args[0]]; print(f"Compressed to {args[0]}.gz")
        else: print(f"gzip: {args[0]}: No such file")

    def cmd_ps(self):
        print("PID   COMMAND")
        for pid, cmd in self.active_procs.items(): print(f"{pid}   {cmd}")

    def cmd_kill(self, args):
        if args and args[0] in self.active_procs: killed = self.active_procs.pop(args[0]); print(f"Killed {killed} (PID {args[0]})")
        else: print("No such process")

    def cmd_curl(self, args):
        if not args: return
        if args[0] == "http://localhost/api/token": print("SECRET_TOKEN_77")
        else: print(f"curl: (6) Could not resolve host: {args[0]}")

    def cmd_find(self, args):
        if len(args) < 3 or args[1] != "-name": print("Usage: find [dir] -name [filename]"); return
        start_dir_str, target_name = args[0], args[2]
        start_path = [p for p in start_dir_str.split("/") if p] if start_dir_str.startswith("/") else (self.cwd + [start_dir_str] if start_dir_str != "." else self.cwd)
        start_node = self.get_node(start_path)
        if not isinstance(start_node, dict) or "content" in start_node: print(f"find: '{start_dir_str}': Not a directory"); return
        def search(node, current_path):
            for k, v in node.items():
                path = current_path + [k]
                if k == target_name: print("/" + "/".join(path))
                if isinstance(v, dict) and "content" not in v: search(v, path)
        search(start_node, start_path)

    def cmd_tar(self, args):
        if len(args) < 2 or args[0] != "-xvf": print("Usage: tar -xvf [file]"); return
        node = self.get_node(self.cwd + [args[1]])
        if isinstance(node, dict) and node.get("type") == "tar":
            self.get_node()[args[1].replace(".tar", ".txt")] = node["content"]
            print(f"Extracted {args[1].replace('.tar', '.txt')}")
        else: print(f"tar: {args[1]}: Not a tar file")

    def cmd_export(self, args):
        if not args or "=" not in args[0]: print("Usage: export VAR=VALUE"); return
        var, val = args[0].split("=", 1)
        self.env_vars[var] = val
        print(f"Exported {var}")

    def cmd_echo(self, args):
        if not args: return
        text = args[0]
        if text.startswith("$"):
            var_name = text[1:]
            print(self.env_vars.get(var_name, ""))
        else:
            print(" ".join(args))

    def cmd_submit(self, args):
        if not args: return
        ans = args[0]
        if self.level == 1 and ans == "SHADOW_NET": print(">> GRANTED!"); self.load_level(2)
        elif self.level == 2 and ans == "ESCALATION_99": print(">> GRANTED!"); self.load_level(3)
        elif self.level == 3 and ans.upper() == "DONE":
            drop = self.get_node(["drop"])
            if drop and "data.txt.gz" in drop: print(">> EXFILTRATED!"); self.load_level(4)
            else: print(">> File belum ada di /drop/")
        elif self.level == 4 and ans == "FLAG_ROOT":
            if "999" not in self.active_procs: print(">> SYSTEM HIJACKED!"); self.load_level(5)
            else: print(">> Firewall masih aktif!")
        elif self.level == 5 and ans == "SECRET_TOKEN_77": print(">> TOKEN ACCEPTED!"); self.load_level(6)
        elif self.level == 6 and ans == "FORENSIC_MASTER": print(">> HIDDEN FILE FOUND!"); self.load_level(7)
        elif self.level == 7 and ans == "3": print(">> LOG ANALYZED!"); self.load_level(8)
        elif self.level == 8 and ans == "OCTAL_KEY_88": print(">> HIDDEN ACCESS GRANTED!"); self.load_level(9)
        elif self.level == 9 and ans == "ARCHIVE_MASTER_99": print(">> PAYLOAD EXTRACTED!"); self.load_level(10)
        elif self.level == 10 and ans == "CYBER_GOD_10": print(">> ENVIRONMENT MASTERED. YOU WIN THE GAME!")
        else: print(">> ACCESS DENIED.")

if __name__ == "__main__":
    TerminalGame().run()