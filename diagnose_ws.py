import frappe
import json

def diagnose():
    frappe.init(site="cng.localhost")
    frappe.connect()
    
    # 1. Check if Workspace exists
    ws = frappe.db.get_value("Workspace", "Kita Management", ["name", "public", "is_hidden", "app", "module"], as_dict=True)
    print(f"Workspace Info: {ws}")
    
    # 2. Get sidebar items
    sidebar_items = frappe.desk.doctype.workspace.workspace.get_workspace_sidebar_items()
    page_names = [p.name for p in sidebar_items.get("pages", [])]
    print(f"Found {len(page_names)} pages in sidebar.")
    print(f"Is 'Kita Management' in sidebar? {'Kita Management' in page_names}")
    
    # 3. Check if DocType is in Workspace
    ws_doc = frappe.get_doc("Workspace", "Kita Management")
    print(f"Links in Workspace: {[l.label for l in ws_doc.links]}")
    
    # 4. Check if Module exits
    module_exists = frappe.db.exists("Module Def", "Kita Management")
    print(f"Module 'Kita Management' exists: {module_exists}")

if __name__ == "__main__":
    diagnose()
