INSERT INTO "public"."g2p_intake_form_ui_tabs" ("tab_id","form_id","tab_label","tab_order") VALUES 
('f3f3a330-98f4-5941-9cec-303e77462b14','852cf76a-a691-5572-9dd2-9bbca6fa5c78','cropsown_intake_tab',10)
ON CONFLICT ("tab_id") DO UPDATE SET
    "form_id" = EXCLUDED."form_id",
    "tab_label" = EXCLUDED."tab_label",
    "tab_order" = EXCLUDED."tab_order";
