<script lang="ts">
    import * as Command from "$lib/components/ui/command";
  </script>
   
  <Command.Root class="w-1/3 h-1/4 outline outline-white">
    <Command.Input placeholder="Type a command or search..." />
    <Command.List>
      <Command.Empty>No results found.</Command.Empty>
      <Command.Separator />
      <Command.Group heading="Companies">
        <Command.Item>Profile</Command.Item>
        <Command.Item>Billing</Command.Item>
        <Command.Item>Settings</Command.Item>
      </Command.Group>
    </Command.List>
  </Command.Root>