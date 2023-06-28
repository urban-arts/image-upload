local HttpService = game:GetService("HttpService")

local url = "http://<your-flask-server-uri>/image_data"

local gridSize = 6
local partSize = 1
local basePosition = Vector3.new(0, partSize / 2, 0)

function deleteRenderedParts()
	for _, part in workspace.RenderParts:GetChildren() do
		if part:IsA('BasePart') then
			part:Destroy()
		end
	end
end

function renderPartsFromServer()
	local response = HttpService:GetAsync(url)
	local imageData = HttpService:JSONDecode(response)
	
	deleteRenderedParts()
	for y = 1, gridSize do
		for x = 1, gridSize do
			local r, g, b = unpack(imageData[y][x])

			local part = Instance.new("Part")
			part.Anchored = true
			part.Size = Vector3.new(partSize, partSize, partSize)
			part.Position = basePosition + Vector3.new(x * partSize, 0, y * partSize)
			part.BrickColor = BrickColor.new(Color3.new(r / 255, g / 255, b / 255))
			part.Parent = workspace.RenderParts
		end
	end
end

-- Handle stuff here
-- For example, I just used a RemoteEvent from the Client to refresh the uploaded image.

game.ReplicatedStorage.RefreshWorkspaceRender.OnServerEvent:Connect(renderPartsFromServer)
